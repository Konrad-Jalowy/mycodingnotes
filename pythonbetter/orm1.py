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

    def close(self):
        self.connection.close()

# Example usage
if __name__ == "__main__":
    orm = SQLiteORM("example.db")

    # Create a table
    orm.create_table("users", {
        "name": "TEXT",
        "email": "TEXT",
        "age": "INTEGER"
    })

    # Insert a record
    user_id = orm.table("users").insert({
        "name": "John Doe",
        "email": "john.doe@example.com",
        "age": 30
    })
    print(f"Inserted user with ID: {user_id}")

    # Query records
    users = orm.table("users").where("age", ">", 25).order_by("name").get()
    print("Users:", users)

    # Update a record
    orm.table("users").update(user_id, {"age": 31})

    # Delete a record
    orm.table("users").delete(user_id)

    # Close connection
    orm.close()
