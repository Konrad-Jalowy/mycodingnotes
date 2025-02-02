import sqlite3
import logging
import re
import csv

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
    """Filtruje użytkowników według podanego kryterium, obsługując zakresy dla wieku."""
    valid_string_columns = {"last_name", "email"}  # Stringi używają LIKE
    valid_int_columns = {"age"}  # Liczby używają >, <, =

    if filter_by not in valid_string_columns and filter_by not in valid_int_columns:
        print(f"⚠ Niepoprawne kryterium filtrowania: {filter_by}. Możesz filtrować po: age, last_name, email.")
        return

    sql = ""
    params = ()

    if filter_by in valid_string_columns:
        # Filtrowanie tekstowe (LIKE %wartość%)
        sql = f"SELECT * FROM users WHERE {filter_by} LIKE ?"
        params = (f"%{filter_value}%",)
    elif filter_by in valid_int_columns:
        # Obsługa warunków <, >, =
        match = re.match(r"([<>]?=?)\s*(\d+)", filter_value)
        if match:
            operator, value = match.groups()
            sql = f"SELECT * FROM users WHERE {filter_by} {operator} ?"
            params = (int(value),)
        else:
            print("⚠ Niepoprawny format dla wieku. Użyj np. `> 25`, `< 30`, `= 40`.")
            return

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(sql, params)
        users = cursor.fetchall()

    if not users:
        print(f"⚠ Brak użytkowników spełniających kryterium {filter_by} {filter_value}.")
        logger.info(f"Brak użytkowników spełniających kryterium {filter_by} {filter_value}.")
    else:
        print(f"\n===== FILTROWANI UŻYTKOWNICY ({filter_by} {filter_value}) =====")
        for user in users:
            print(f"ID: {user[0]} | {user[1]} {user[2]} | Email: {user[3]} | Wiek: {user[4]}")
        logger.info(f"Wyświetlono użytkowników spełniających kryterium {filter_by} {filter_value}.")


def export_to_csv():
    """Eksportuje użytkowników do pliku CSV z możliwością podania własnej nazwy."""
    filename = input("Podaj nazwę pliku do eksportu (ENTER = `users.csv`): ") or "users.csv"

    sql = "SELECT * FROM users"

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        users = cursor.fetchall()

    if not users:
        print("⚠ Brak użytkowników do eksportu.")
        logger.info("Brak użytkowników do eksportu.")
        return

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Imię", "Nazwisko", "Email", "Wiek"])
        writer.writerows(users)

    print(f"✅ Eksport zakończony! Dane zapisane w `{filename}`.")
    logger.info(f"Wyeksportowano {len(users)} użytkowników do pliku {filename}.")


def import_from_csv():
    """Importuje użytkowników z pliku CSV z możliwością podania własnej nazwy."""
    filename = input("Podaj nazwę pliku do importu (ENTER = `import_users.csv`): ") or "import_users.csv"

    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader)

            added_count = 0
            skipped_count = 0

            with sqlite3.connect(DB_NAME) as conn:
                cursor = conn.cursor()

                for row in reader:
                    if len(row) != 5:
                        print(f"⚠ Pominięto niepoprawny wiersz: {row}")
                        continue

                    _, first_name, last_name, email, age = row

                    try:
                        cursor.execute(
                            "INSERT INTO users (first_name, last_name, email, age) VALUES (?, ?, ?, ?)",
                            (first_name, last_name, email, int(age))
                        )
                        added_count += 1
                    except sqlite3.IntegrityError:
                        print(f"⚠ Użytkownik `{email}` już istnieje – pominięto.")
                        skipped_count += 1

                conn.commit()

        print(f"✅ Import zakończony! Dodano {added_count} użytkowników, pominięto {skipped_count}.")
        logger.info(f"Import zakończony! Dodano {added_count} użytkowników, pominięto {skipped_count}.")

    except FileNotFoundError:
        print(f"❌ Plik `{filename}` nie został znaleziony.")
        logger.error(f"Plik `{filename}` nie został znaleziony.")


def update_user(user_id):
    """Edytuje użytkownika, pozwalając na zachowanie aktualnych wartości."""
    sql_select = "SELECT first_name, last_name, email, age FROM users WHERE id = ?"

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(sql_select, (user_id,))
        user = cursor.fetchone()

        if not user:
            print(f"❌ Nie znaleziono użytkownika o ID {user_id}.")
            return

        print("\n===== Edytowanie użytkownika =====")
        print(f"Aktualne dane: {user[0]} {user[1]} | Email: {user[2]} | Wiek: {user[3]}")

        first_name = input(f"Nowe imię (ENTER, aby zostawić `{user[0]}`): ") or user[0]
        last_name = input(f"Nowe nazwisko (ENTER, aby zostawić `{user[1]}`): ") or user[1]
        email = input(f"Nowy email (ENTER, aby zostawić `{user[2]}`): ") or user[2]
        age = input(f"Nowy wiek (ENTER, aby zostawić `{user[3]}`): ") or user[3]

        try:
            age = int(age)
        except ValueError:
            print("⚠ Wiek musi być liczbą! Operacja anulowana.")
            return

        sql_update = """
        UPDATE users
        SET first_name = ?, last_name = ?, email = ?, age = ?
        WHERE id = ?
        """

        cursor.execute(sql_update, (first_name, last_name, email, age, user_id))
        conn.commit()

        print("✅ Użytkownik został zaktualizowany.")
        logger.info(f"Zaktualizowano użytkownika ID {user_id}: {first_name} {last_name}, Email: {email}, Wiek: {age}")