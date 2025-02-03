from database.db_connector import initialize_database
from repositories.user_repository import UserRepository
from models.user import User

def main():
    initialize_database()
    user_repo = UserRepository()

    # Dodajemy użytkowników
    user1 = user_repo.add_user(User(username="john_doe", email="john@example.com"))
    user2 = user_repo.add_user(User(username="jane_doe", email="jane@example.com"))

    print("\n✅ Użytkownicy po dodaniu:")
    print(user_repo.get_all_users())

    # Pobieramy użytkownika
    print("\n🔎 Pobieramy użytkownika o ID 1:")
    user = user_repo.get_user_by_id(1)
    print(user)

    # Usuwamy użytkownika
    print("\n🗑️ Usuwamy użytkownika o ID 1...")
    user_repo.delete_user(1)

    print("\n✅ Użytkownicy po usunięciu:")
    print(user_repo.get_all_users())

if __name__ == "__main__":
    main()
