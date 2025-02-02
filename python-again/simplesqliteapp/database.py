import sqlite3

DB_NAME = "users.db"

def create_table():
    """Tworzy tabelę użytkowników w bazie danych."""
    sql = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        age INTEGER
    )
    """
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

# Automatyczne utworzenie tabeli przy imporcie
create_table()
