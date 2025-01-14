import sqlite3
from typing import Any, Dict, List, Optional

class SQLiteORM:
    def __init__(self, db_path: str):
        self.connection = sqlite3.connect(db_path)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        self._table = ""
        self._conditions = []
        self._order_by_clauses = []
        self._limit_value = 0
        self._offset_value = 0

    def table(self, table_name: str):
        self._table = table_name
        self._conditions = []
        self._order_by_clauses = []
        self._limit_value = 0
        self._offset_value = 0
        return self

    def where(self, column: str, operator: str, value: Any):
        self._conditions.append((column, operator, value))
        return self

    def order_by(self, column: str, direction: str = "ASC"):
        self._order_by_clauses.append(f"{column} {direction}")
        return self

    def limit(self, limit: int):
        self._limit_value = limit
        return self

    def offset(self, offset: int):
        self._offset_value = offset
        return self

    def get(self) -> List[Dict[str, Any]]:
        query = f"SELECT * FROM {self._table}"

        if self._conditions:
            condition_str = " AND ".join([f"{col} {op} ?" for col, op, _ in self._conditions])
            query += f" WHERE {condition_str}"

        if self._order_by_clauses:
            query += f" ORDER BY {', '.join(self._order_by_clauses)}"

        if self._limit_value:
            query += f" LIMIT {self._limit_value}"

        if self._offset_value:
            query += f" OFFSET {self._offset_value}"

        params = [value for _, _, value in self._conditions]
        self.cursor.execute(query, params)
        return [dict(row) for row in self.cursor.fetchall()]

    def first(self) -> Optional[Dict[str, Any]]:
        self.limit(1)
        results = self.get()
        return results[0] if results else None

    def insert(self, data: Dict[str, Any]) -> int:
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["?" for _ in data])
        query = f"INSERT INTO {self._table} ({columns}) VALUES ({placeholders})"
        self.cursor.execute(query, tuple(data.values()))
        self.connection.commit()
        return self.cursor.lastrowid

    def update(self, id: int, data: Dict[str, Any]) -> bool:
        set_clause = ", ".join([f"{key} = ?" for key in data])
        query = f"UPDATE {self._table} SET {set_clause} WHERE id = ?"
        self.cursor.execute(query, tuple(data.values()) + (id,))
        self.connection.commit()
        return self.cursor.rowcount > 0

    def delete(self, id: int) -> bool:
        query = f"DELETE FROM {self._table} WHERE id = ?"
        self.cursor.execute(query, (id,))
        self.connection.commit()
        return self.cursor.rowcount > 0

    def create_table(self, table_name: str, columns: Dict[str, str]):
        column_definitions = ", ".join([f"{name} {type}" for name, type in columns.items()])
        query = f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, {column_definitions})"
        self.cursor.execute(query)
        self.connection.commit()

    def has_many(self, related_table: str, foreign_key: str, local_key: str = "id") -> List[Dict[str, Any]]:
        query = f"SELECT * FROM {related_table} WHERE {foreign_key} = ?"
        self.cursor.execute(query, (self._conditions[0][2],))
        return [dict(row) for row in self.cursor.fetchall()]

    def belongs_to(self, related_table: str, foreign_key: str, local_key: str = "id") -> Optional[Dict[str, Any]]:
        query = f"SELECT * FROM {related_table} WHERE {local_key} = ?"
        self.cursor.execute(query, (foreign_key,))
        row = self.cursor.fetchone()
        return dict(row) if row else None

    def many_to_many(self, join_table: str, related_table: str, related_key: str, local_key: str, foreign_key: str) -> List[Dict[str, Any]]:
        query = f"""
        SELECT DISTINCT {related_table}.* 
        FROM {related_table}
        INNER JOIN {join_table} ON {join_table}.{related_key} = {related_table}.id
        WHERE {join_table}.{foreign_key} = ?
        """
        params = (self._conditions[0][2],) if self._conditions else ()
        self.cursor.execute(query, params)
        return [dict(row) for row in self.cursor.fetchall()]

    def close(self):
        self.connection.close()

# Example usage
if __name__ == "__main__":
    orm = SQLiteORM("example.db")

    # Create tables
    orm.create_table("users", {
        "name": "TEXT",
        "email": "TEXT",
        "age": "INTEGER"
    })

    orm.create_table("projects", {
        "name": "TEXT",
        "description": "TEXT"
    })

    orm.create_table("user_projects", {
        "user_id": "INTEGER",
        "project_id": "INTEGER"
    })

    # Insert users
    user1_id = orm.table("users").insert({"name": "Alice", "email": "alice@example.com", "age": 25})
    user2_id = orm.table("users").insert({"name": "Bob", "email": "bob@example.com", "age": 30})

    # Insert projects
    project1_id = orm.table("projects").insert({"name": "Project A", "description": "First project"})
    project2_id = orm.table("projects").insert({"name": "Project B", "description": "Second project"})

    # Link users and projects (many-to-many relationship)
    orm.table("user_projects").insert({"user_id": user1_id, "project_id": project1_id})
    orm.table("user_projects").insert({"user_id": user1_id, "project_id": project2_id})
    orm.table("user_projects").insert({"user_id": user2_id, "project_id": project1_id})

    # Query projects for a specific user
    user_projects = orm.table("users").where("id", "=", user1_id).many_to_many("user_projects", "projects", "project_id", "user_id", "user_id")
    print("Projects for Alice:", user_projects)

    # Query users for a specific project
    project_users = orm.table("projects").where("id", "=", project1_id).many_to_many("user_projects", "users", "user_id", "project_id", "project_id")
    print("Users in Project A:", project_users)

    orm.close()
