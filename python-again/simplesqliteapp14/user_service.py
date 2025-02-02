import csv
from models import User, SessionLocal


def add_user(first_name, last_name, email, age):
    """Dodaje nowego użytkownika do bazy."""
    session = SessionLocal()
    try:
        user = User(first_name=first_name, last_name=last_name, email=email, age=age)
        session.add(user)
        session.commit()
        print("✅ Użytkownik dodany!")
    except Exception as e:
        session.rollback()
        print(f"❌ Błąd: {e}")
    finally:
        session.close()


def list_users():
    """Wyświetla listę użytkowników."""
    session = SessionLocal()
    users = session.query(User).all()

    if not users:
        print("⚠ Brak użytkowników w bazie.")
    else:
        print("\n===== LISTA UŻYTKOWNIKÓW =====")
        for user in users:
            print(user)  # Dzięki __str__() w modelu automatycznie wyświetli format ID: ... | Imię | Email | Wiek

    session.close()


def update_user(user_id):
    """Edytuje użytkownika, pokazując aktualne wartości i podsumowując zmiany."""
    session = SessionLocal()
    user = session.query(User).filter_by(id=user_id).first()

    if not user:
        print(f"❌ Nie znaleziono użytkownika o ID {user_id}.")
        session.close()
        return

    print("\n===== Edytowanie użytkownika =====")
    print(f"Aktualne dane: {user}")  # Automatyczne formatowanie z __str__()

    first_name = input(f"Nowe imię (ENTER = `{user.first_name}`): ") or user.first_name
    last_name = input(f"Nowe nazwisko (ENTER = `{user.last_name}`): ") or user.last_name
    email = input(f"Nowy email (ENTER = `{user.email}`): ") or user.email
    age_input = input(f"Nowy wiek (ENTER = `{user.age}`): ") or str(user.age)

    try:
        age = int(age_input)
    except ValueError:
        print("⚠ Wiek musi być liczbą! Operacja anulowana.")
        session.close()
        return

    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.age = age

    session.commit()

    print("\n✅ Użytkownik został zaktualizowany. Nowe dane:")
    print(user)  # Automatycznie wypisze poprawiony format

    session.close()


def delete_user(user_id):
    """Usuwa użytkownika."""
    session = SessionLocal()
    user = session.query(User).filter_by(id=user_id).first()

    if not user:
        print(f"❌ Nie znaleziono użytkownika o ID {user_id}.")
        session.close()
        return

    session.delete(user)
    session.commit()
    print(f"✅ Użytkownik ID {user_id} został usunięty.")
    session.close()


def export_to_csv():
    """Eksportuje użytkowników do pliku CSV z możliwością podania własnej nazwy."""
    filename = input("Podaj nazwę pliku do eksportu (ENTER = `users.csv`): ") or "users.csv"

    session = SessionLocal()
    users = session.query(User).all()

    if not users:
        print("⚠ Brak użytkowników do eksportu.")
        session.close()
        return

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Imię", "Nazwisko", "Email", "Wiek"])
        for user in users:
            writer.writerow([user.id, user.first_name, user.last_name, user.email, user.age])

    print(f"✅ Eksport zakończony! Dane zapisane w `{filename}`.")
    session.close()


def import_from_csv():
    """Importuje użytkowników z pliku CSV z możliwością podania własnej nazwy."""
    filename = input("Podaj nazwę pliku do importu (ENTER = `import_users.csv`): ") or "import_users.csv"

    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader)  # Pomijamy nagłówki

            added_count = 0
            skipped_count = 0

            session = SessionLocal()

            for row in reader:
                if len(row) != 5:  # Sprawdzamy, czy są wszystkie kolumny
                    print(f"⚠ Pominięto niepoprawny wiersz: {row}")
                    continue

                _, first_name, last_name, email, age = row  # Pomijamy ID

                # Sprawdzamy, czy użytkownik z tym e-mailem już istnieje
                if session.query(User).filter_by(email=email).first():
                    print(f"⚠ Użytkownik `{email}` już istnieje – pominięto.")
                    skipped_count += 1
                    continue

                user = User(first_name=first_name, last_name=last_name, email=email, age=int(age))
                session.add(user)
                added_count += 1

            session.commit()
            session.close()

        print(f"✅ Import zakończony! Dodano {added_count} użytkowników, pominięto {skipped_count}.")

    except FileNotFoundError:
        print(f"❌ Plik `{filename}` nie został znaleziony.")
