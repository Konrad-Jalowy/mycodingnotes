import user_service
import task_service

def menu():
    while True:
        print("\n===== MENU =====")
        print("1. Dodaj użytkownika")
        print("2. Wyświetl użytkowników")
        print("3. Edytuj użytkownika")
        print("4. Usuń użytkownika")
        print("5. Dodaj zadanie")
        print("6. Wyświetl zadania")
        print("7. Edytuj zadanie")
        print("8. Usuń zadanie")
        print("9. Wyjście")
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
            user_id = input("Podaj ID użytkownika, do którego przypisać zadanie: ")
            title = input("Tytuł zadania: ")
            description = input("Opis zadania: ")
            task_service.add_task(user_id, title, description)
        elif choice == "6":
            user_id = input("Podaj ID użytkownika (ENTER = wszystkie zadania): ") or None
            task_service.list_tasks(user_id)
        elif choice == "7":
            task_id = input("Podaj ID zadania do edycji: ")
            task_service.update_task(task_id)
        elif choice == "8":
            task_id = input("Podaj ID zadania do usunięcia: ")
            task_service.delete_task(task_id)
        elif choice == "9":
            print("👋 Zamykanie aplikacji...")
            break
        else:
            print("⚠ Niepoprawny wybór!")

if __name__ == "__main__":
    menu()
