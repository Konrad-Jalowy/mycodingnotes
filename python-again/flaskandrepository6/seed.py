from faker import Faker
from database.db_connector import db
from models.user import User
from flask import current_app

fake = Faker()


def seed_users(n=20):
    """Generuje n fejkowych użytkowników i zapisuje do bazy."""
    with current_app.app_context():  # ✅ Używamy current_app, zamiast importować `app`
        db.drop_all()  # Usunięcie starej bazy (opcjonalnie)
        db.create_all()  # Tworzymy tabelę jeśli nie istnieje

        users = []
        for _ in range(n):
            user = User(
                username=fake.user_name(),
                email=fake.email()
            )
            users.append(user)

        db.session.add_all(users)
        db.session.commit()

        print(f"✅ Dodano {n} fejkowych użytkowników!")


if __name__ == "__main__":
    seed_users(50)  # Możesz zmienić liczbę użytkowników
