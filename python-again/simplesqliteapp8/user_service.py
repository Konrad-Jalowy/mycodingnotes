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


def update_user(user_id, first_name=None, last_name=None, email=None, age=None):
    """Aktualizuje użytkownika."""
    session = Session()
    user = session.query(User).filter_by(id=user_id).first()

    if not user:
        print(f"❌ Nie znaleziono użytkownika o ID {user_id}.")
        return

    if first_name:
        user.first_name = first_name
    if last_name:
        user.last_name = last_name
    if email:
        user.email = email
    if age:
        user.age = age

    session.commit()
    print(f"✅ Zaktualizowano użytkownika ID {user_id}.")
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

