from sqlalchemy.orm import sessionmaker
from models import User, engine

# Tworzymy nową sesję
Session = sessionmaker(bind=engine)


def add_user(first_name, last_name, email, age):
    """Dodaje nowego użytkownika do bazy."""
    session = Session()
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
    session = Session()
    users = session.query(User).all()

    if not users:
        print("⚠ Brak użytkowników w bazie.")
    else:
        print("\n===== LISTA UŻYTKOWNIKÓW =====")
        for user in users:
            print(f"ID: {user.id} | {user.first_name} {user.last_name} | Email: {user.email} | Wiek: {user.age}")

    session.close()


def update_user(user_id):
    """Edytuje użytkownika, pokazując aktualne wartości i podsumowując zmiany."""
    session = Session()
    user = session.query(User).filter_by(id=user_id).first()

    if not user:
        print(f"❌ Nie znaleziono użytkownika o ID {user_id}.")
        return

    print("\n===== Edytowanie użytkownika =====")
    print(f"Aktualne dane: {user.first_name} {user.last_name} | Email: {user.email} | Wiek: {user.age}")

    first_name = input(f"Nowe imię (ENTER = `{user.first_name}`): ") or user.first_name
    last_name = input(f"Nowe nazwisko (ENTER = `{user.last_name}`): ") or user.last_name
    email = input(f"Nowy email (ENTER = `{user.email}`): ") or user.email
    age_input = input(f"Nowy wiek (ENTER = `{user.age}`): ") or str(user.age)

    try:
        age = int(age_input)
    except ValueError:
        print("⚠ Wiek musi być liczbą! Operacja anulowana.")
        return

    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.age = age

    session.commit()

    print("\n✅ Użytkownik został zaktualizowany. Nowe dane:")
    print(f"ID: {user.id} | {user.first_name} {user.last_name} | Email: {user.email} | Wiek: {user.age}")

    session.close()


def delete_user(user_id):
    """Usuwa użytkownika."""
    session = Session()
    user = session.query(User).filter_by(id=user_id).first()

    if not user:
        print(f"❌ Nie znaleziono użytkownika o ID {user_id}.")
        return

    session.delete(user)
    session.commit()
    print(f"✅ Użytkownik ID {user_id} został usunięty.")
    session.close()
