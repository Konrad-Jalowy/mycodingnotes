import click
from flask import current_app
from faker import Faker
from app.models import User, Group

fake = Faker()

@click.command("seed")
@click.option("--random", is_flag=True, help="Dodaje losowe dane (Faker)")
def seed_database(random):
    """ Wypełnia bazę testowymi danymi """
    from app import db  # 🔹 Importujemy `db` wewnątrz funkcji, aby uniknąć cyklicznego importu

    with current_app.app_context():
        db.drop_all()
        db.create_all()

        if random:
            click.echo("🔹 Seeding losowymi danymi...")
            seed_random_data(db)
        else:
            click.echo("🔹 Seeding ustalonymi danymi...")
            seed_static_data(db)

        db.session.commit()
        click.echo("✅ Seeding zakończony!")

def seed_static_data(db):
    """ Seeding ustalonych danych """
    users = [
        User(username="Janek"),
        User(username="Kasia"),
        User(username="Marek")
    ]
    groups = [
        Group(name="Python Devs"),
        Group(name="AI Enthusiasts"),
        Group(name="Web Developers")
    ]

    db.session.add_all(users)
    db.session.add_all(groups)
    db.session.commit()

    # Dodanie użytkowników do grup
    users[0].groups.append(groups[0])  # Janek → Python Devs
    users[1].groups.append(groups[0])  # Kasia → Python Devs
    users[0].groups.append(groups[1])  # Janek → AI Enthusiasts
    users[2].groups.append(groups[2])  # Marek → Web Developers
    db.session.commit()

def seed_random_data(db):
    """ Seeding losowych danych za pomocą Faker """
    users = [User(username=fake.first_name()) for _ in range(10)]
    groups = [Group(name=fake.company()) for _ in range(5)]

    db.session.add_all(users)
    db.session.add_all(groups)
    db.session.commit()

    # Przypisujemy użytkowników do losowych grup
    for user in users:
        random_groups = fake.random_elements(elements=groups, length=2, unique=True)
        user.groups.extend(random_groups)
    db.session.commit()
