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
        print("6. Wyświetl użytkowników (posortowanych)")
        print("7. Filtrowanie użytkowników")
        print("8. Eksportuj użytkowników do CSV")
        print("9. Importuj użytkowników z CSV")
        print("10. Wyjście")
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
            order_by = input("Sortować po: (id, first_name, last_name, email, age): ")
            user_service.list_users(order_by)
        elif choice == "7":
            filter_by = input("Filtruj po: (age, last_name, email): ")
            filter_value = input("Podaj wartość (dla wieku: < 30, > 25, = 40): ")
            user_service.filter_users(filter_by, filter_value)
        elif choice == "8":
            user_service.export_to_csv()
        elif choice == "9":
            user_service.import_from_csv()
        elif choice == "10":
            print("👋 Zamykanie aplikacji...")
            break
        else:
            print("⚠ Niepoprawny wybór!")

if __name__ == "__main__":
    menu()
