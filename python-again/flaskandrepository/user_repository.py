from database.db_connector import get_connection
from models.user import User

class UserRepository:
    """Repozytorium do obsługi użytkowników."""

    def add_user(self, user):
        """Dodaje użytkownika do bazy."""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", (user.username, user.email))
            conn.commit()
            user.id = cursor.lastrowid  # Pobranie ID nowo dodanego użytkownika
        return user

    def get_user_by_id(self, user_id):
        """Pobiera użytkownika na podstawie ID."""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
            row = cursor.fetchone()
            return User(*row) if row else None

    def get_all_users(self):
        """Zwraca listę wszystkich użytkowników."""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users")
            rows = cursor.fetchall()
            return [User(*row) for row in rows]

    def delete_user(self, user_id):
        """Usuwa użytkownika z bazy."""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
            conn.commit()
            return cursor.rowcount  # Liczba usuniętych rekordów
