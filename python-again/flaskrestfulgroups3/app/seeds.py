import click
from flask import current_app
from app import db
from app.models import User, Group
from faker import Faker

fake = Faker()

@click.command("seed")
@click.option("--random", is_flag=True, help="Dodaje losowe dane (Faker)")
def seed_database(random):
    """ Wypełnia bazę testowymi danymi """
    with current_app.app_context():
        db.drop_all()  # Usuwamy tabelki
        db.create_all()  # Tworzymy je ponownie

        if random:
            click.echo("🔹 Seeding losowymi danymi...")
            seed_random_data()
        else:
            click.echo("🔹 Seeding ustalonymi danymi...")
            seed_static_data()

        db.session.commit()
        click.echo("✅ Seeding zakończony!")

def seed_static_data():
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

def seed_random_data():
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
