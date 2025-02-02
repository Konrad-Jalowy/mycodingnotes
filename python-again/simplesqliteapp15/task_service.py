from models import Task, User, SessionLocal


def add_task(user_id, title, description):
    """Dodaje zadanie do użytkownika."""
    session = SessionLocal()
    user = session.query(User).filter_by(id=user_id).first()

    if not user:
        print(f"❌ Nie znaleziono użytkownika o ID {user_id}.")
        session.close()
        return

    task = Task(title=title, description=description, user_id=user_id)
    session.add(task)
    session.commit()

    print(f"✅ Dodano zadanie: {task.title} dla użytkownika {user.first_name} {user.last_name}.")
    session.close()


def list_tasks(user_id=None):
    """Wyświetla zadania użytkownika lub wszystkich użytkowników."""
    session = SessionLocal()

    if user_id:
        tasks = session.query(Task).filter_by(user_id=user_id).all()
    else:
        tasks = session.query(Task).all()

    if not tasks:
        print("⚠ Brak zadań.")
    else:
        print("\n===== LISTA ZADAŃ =====")
        for task in tasks:
            print(task)  # Dzięki __str__() automatycznie wyświetli format

    session.close()


def update_task(task_id):
    """Edytuje zadanie, pokazując aktualne wartości i podsumowując zmiany."""
    session = SessionLocal()
    task = session.query(Task).filter_by(id=task_id).first()

    if not task:
        print(f"❌ Nie znaleziono zadania o ID {task_id}.")
        session.close()
        return

    print("\n===== Edytowanie zadania =====")
    print(f"Aktualne dane: {task}")  # Automatyczne formatowanie z __str__()

    title = input(f"Nowy tytuł (ENTER = `{task.title}`): ") or task.title
    description = input(f"Nowy opis (ENTER = `{task.description or 'Brak'}`): ") or task.description
    status = input(f"Nowy status (`pending`, `in progress`, `completed`) (ENTER = `{task.status}`): ") or task.status

    task.title = title
    task.description = description
    task.status = status

    session.commit()

    print("\n✅ Zadanie zostało zaktualizowane. Nowe dane:")
    print(task)  # Automatycznie wypisze poprawiony format

    session.close()


def delete_task(task_id):
    """Usuwa zadanie."""
    session = SessionLocal()
    task = session.query(Task).filter_by(id=task_id).first()

    if not task:
        print(f"❌ Nie znaleziono zadania o ID {task_id}.")
        session.close()
        return

    session.delete(task)
    session.commit()
    print(f"✅ Zadanie `{task.title}` zostało usunięte.")
    session.close()
