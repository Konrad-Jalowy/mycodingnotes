import user_service

def menu():
    while True:
        print("\n===== MENU =====")
        print("1. Dodaj użytkownika")
        print("2. Wyświetl użytkowników")
        print("3. Edytuj użytkownika")
        print("4. Usuń użytkownika")
        print("5. Eksportuj użytkowników do CSV")
        print("6. Importuj użytkowników z CSV")
        print("7. Wyjście")
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
            user_id = input("Podaj ID użytkownika do edycji: ")
            user_service.update_user(user_id)
        elif choice == "4":
            user_id = input("Podaj ID użytkownika: ")
            user_service.delete_user(user_id)
        elif choice == "5":
            user_service.export_to_csv()
        elif choice == "6":
            user_service.import_from_csv()
        elif choice == "7":
            print("👋 Zamykanie aplikacji...")
            break
        else:
            print("⚠ Niepoprawny wybór!")

if __name__ == "__main__":
    menu()
