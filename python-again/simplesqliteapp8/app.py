import user_service

def menu():
    while True:
        print("\n===== MENU =====")
        print("1. Dodaj użytkownika")
        print("2. Wyświetl użytkowników")
        print("3. Edytuj użytkownika")
        print("4. Usuń użytkownika")
        print("5. Wyjście")
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
            user_id = input("Podaj ID użytkownika: ")
            first_name = input("Nowe imię (ENTER = brak zmian): ")
            last_name = input("Nowe nazwisko (ENTER = brak zmian): ")
            email = input("Nowy email (ENTER = brak zmian): ")
            age = input("Nowy wiek (ENTER = brak zmian): ")

            first_name = first_name if first_name else None
            last_name = last_name if last_name else None
            email = email if email else None
            age = int(age) if age else None

            user_service.update_user(user_id, first_name, last_name, email, age)
        elif choice == "4":
            user_id = input("Podaj ID użytkownika: ")
            user_service.delete_user(user_id)
        elif choice == "5":
            print("👋 Zamykanie aplikacji...")
            break
        else:
            print("⚠ Niepoprawny wybór!")

if __name__ == "__main__":
    menu()
