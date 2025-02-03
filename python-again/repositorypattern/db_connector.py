import sqlite3

DB_PATH = "database.db"

def get_connection():
    """Tworzy i zwraca połączenie z bazą SQLite."""
    return sqlite3.connect(DB_PATH)

def initialize_database():
    """Tworzy tabelę users, jeśli nie istnieje."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE
            );
        """)
        conn.commit()
