import typer
from models import SessionLocal, User, Address, Task, Hashtag

app = typer.Typer()

# Funkcja do tworzenia sesji
def get_session():
    return SessionLocal()

@app.command()
def add_user(name: str):
    """Dodaj użytkownika"""
    session = get_session()
    user = User(name=name)
    session.add(user)
    session.commit()
    typer.echo(f"Użytkownik '{name}' dodany!")

@app.command()
def add_address(user_id: int, street: str, city: str):
    """Dodaj adres do użytkownika"""
    session = get_session()
    user = session.get(User, user_id)
    if user:
        address = Address(street=street, city=city, user=user)
        session.add(address)
        session.commit()
        typer.echo(f"Adres '{street}, {city}' dodany do użytkownika '{user.name}'.")
    else:
        typer.echo("Użytkownik nie istnieje.")

@app.command()
def add_task(user_id: int, description: str):
    """Dodaj zadanie do użytkownika"""
    session = get_session()
    user = session.get(User, user_id)
    if user:
        task = Task(description=description, user=user)
        session.add(task)
        session.commit()
        typer.echo(f"Zadanie '{description}' dodane do użytkownika '{user.name}'.")
    else:
        typer.echo("Użytkownik nie istnieje.")

@app.command()
def add_hashtag(name: str):
    """Dodaj hasztag"""
    session = get_session()
    hashtag = Hashtag(name=name)
    session.add(hashtag)
    session.commit()
    typer.echo(f"Hasztag '#{name}' dodany.")

@app.command()
def assign_hashtag(task_id: int, hashtag_id: int):
    """Przypisz hasztag do zadania"""
    session = get_session()
    task = session.get(Task, task_id)
    hashtag = session.get(Hashtag, hashtag_id)
    if task and hashtag:
        task.hashtags.append(hashtag)
        session.commit()
        typer.echo(f"Hasztag '#{hashtag.name}' przypisany do zadania '{task.description}'.")
    else:
        typer.echo("Nie znaleziono zadania lub hasztagu.")

@app.command()
def list_users():
    """Lista użytkowników i ich relacji"""
    session = get_session()
    users = session.query(User).all()
    for user in users:
        typer.echo(f"Użytkownik: {user.name}")
        if user.address:
            typer.echo(f"  Adres: {user.address.street}, {user.address.city}")
        if user.tasks:
            for task in user.tasks:
                typer.echo(f"  Zadanie: {task.description} (Hasztagi: {[h.name for h in task.hashtags]})")
    session.close()

if __name__ == "__main__":
    app()
