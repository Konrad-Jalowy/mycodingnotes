import user_service
import database
def menu():
    while True:
        print("\n===== MENU =====")
        print("1. Dodaj użytkownika")
        print("2. Wyświetl użytkowników")
        print("3. Wyszukaj użytkownika po nazwisku")
        print("4. Zmień wiek użytkownika")
        print("5. Usuń użytkownika")
        print("6. Wyjście")
        choice = input("Wybierz opcję: ")

        if choice == "1":
            first_name = input("Imię: ")
            last_name = input("Nazwisko: ")
            email = input("Email: ")
            age = input("Wiek: ")
            user_service.add_user(first_name, last_name, email, age)
        elif choice == "2":
            user_service.list_users()
        elif choice == "3":
            last_name = input("Podaj nazwisko: ")
            user_service.search_user_by_last_name(last_name)
        elif choice == "4":
            user_id = input("Podaj ID użytkownika: ")
            new_age = input("Nowy wiek: ")
            user_service.update_user_age(user_id, new_age)
        elif choice == "5":
            user_id = input("Podaj ID użytkownika: ")
            user_service.delete_user(user_id)
        elif choice == "6":
            print("👋 Zamykanie aplikacji...")
            break
        else:
            print("⚠ Niepoprawny wybór!")

if __name__ == "__main__":
    menu()
