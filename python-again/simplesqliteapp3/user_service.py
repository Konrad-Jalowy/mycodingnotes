import sqlite3
import logging

DB_NAME = "users.db"

# Konfiguracja logowania
logging.basicConfig(filename="app.log", level=logging.INFO,
                    format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

def add_user(first_name, last_name, email, age):
    """Dodaje nowego użytkownika do bazy."""
    sql = "INSERT INTO users (first_name, last_name, email, age) VALUES (?, ?, ?, ?)"
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (first_name, last_name, email, age))
            conn.commit()
            logger.info(f"Dodano użytkownika: {first_name} {last_name}, Email: {email}")
            print("✅ Użytkownik dodany!")
    except sqlite3.IntegrityError:
        logger.warning(f"Nie udało się dodać użytkownika – email {email} już istnieje!")
        print("❌ Błąd: Użytkownik o tym emailu już istnieje.")


def list_users(order_by="id"):
    """Wyświetla listę użytkowników posortowaną według wybranego pola."""
    valid_columns = {"id", "first_name", "last_name", "email", "age"}
    if order_by not in valid_columns:
        print(f"⚠ Niepoprawna kolumna sortowania: {order_by}. Domyślnie sortujemy po ID.")
        order_by = "id"

    sql = f"SELECT * FROM users ORDER BY {order_by} ASC"

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        users = cursor.fetchall()

    if not users:
        print("⚠ Brak użytkowników w bazie.")
        logger.info("Brak użytkowników w bazie.")
    else:
        print(f"\n===== LISTA UŻYTKOWNIKÓW (Sortowanie po: {order_by}) =====")
        for user in users:
            print(f"ID: {user[0]} | {user[1]} {user[2]} | Email: {user[3]} | Wiek: {user[4]}")
        logger.info(f"Wyświetlono listę użytkowników posortowaną po {order_by}.")


def search_user_by_last_name(last_name):
    """Wyszukuje użytkownika po nazwisku."""
    sql = "SELECT * FROM users WHERE last_name LIKE ?"
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(sql, (f"%{last_name}%",))
        users = cursor.fetchall()

    if not users:
        print(f"⚠ Brak użytkowników o nazwisku '{last_name}'.")
        logger.info(f"Brak użytkowników o nazwisku '{last_name}'.")
    else:
        print("\n🔍 ZNALEZIONI UŻYTKOWNICY:")
        for user in users:
            print(f"ID: {user[0]} | {user[1]} {user[2]} | Email: {user[3]} | Wiek: {user[4]}")
        logger.info(f"Wyszukano użytkowników o nazwisku '{last_name}'.")

def update_user_age(user_id, new_age):
    """Aktualizuje wiek użytkownika."""
    sql = "UPDATE users SET age = ? WHERE id = ?"
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(sql, (new_age, user_id))
        if cursor.rowcount > 0:
            conn.commit()
            print(f"✅ Zaktualizowano wiek użytkownika ID: {user_id}.")
            logger.info(f"Zaktualizowano wiek użytkownika ID: {user_id} do {new_age} lat.")
        else:
            print(f"❌ Nie znaleziono użytkownika o ID {user_id}.")

def delete_user(user_id):
    """Usuwa użytkownika na podstawie ID."""
    sql = "DELETE FROM users WHERE id = ?"
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(sql, (user_id,))
        if cursor.rowcount > 0:
            conn.commit()
            print(f"✅ Użytkownik ID: {user_id} został usunięty.")
            logger.info(f"Usunięto użytkownika ID: {user_id}.")
        else:
            print(f"❌ Nie znaleziono użytkownika o ID {user_id}.")


def filter_users(filter_by, filter_value):
    """Filtruje użytkowników według podanego kryterium."""
    valid_columns = {"age", "last_name", "email"}
    if filter_by not in valid_columns:
        print(f"⚠ Niepoprawne kryterium filtrowania: {filter_by}. Możesz filtrować po: age, last_name, email.")
        return

    sql = f"SELECT * FROM users WHERE {filter_by} LIKE ?"

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(sql, (f"%{filter_value}%",))
        users = cursor.fetchall()

    if not users:
        print(f"⚠ Brak użytkowników spełniających kryterium {filter_by} = {filter_value}.")
        logger.info(f"Brak użytkowników spełniających kryterium {filter_by} = {filter_value}.")
    else:
        print(f"\n===== FILTROWANI UŻYTKOWNICY ({filter_by} = {filter_value}) =====")
        for user in users:
            print(f"ID: {user[0]} | {user[1]} {user[2]} | Email: {user[3]} | Wiek: {user[4]}")
        logger.info(f"Wyświetlono użytkowników spełniających kryterium {filter_by} = {filter_value}.")
