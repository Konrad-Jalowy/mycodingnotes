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


def update_task(task_id, title=None, description=None, status=None):
    """Aktualizuje zadanie."""
    session = SessionLocal()
    task = session.query(Task).filter_by(id=task_id).first()

    if not task:
        print(f"❌ Nie znaleziono zadania o ID {task_id}.")
        session.close()
        return

    if title:
        task.title = title
    if description:
        task.description = description
    if status:
        task.status = status

    session.commit()
    print(f"✅ Zadanie `{task.title}` zostało zaktualizowane.")
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
