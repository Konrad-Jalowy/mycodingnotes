import click
from flask import Blueprint
from app.extensions import db
from app.models import Movie, Actor, Director, Category, Review

cli_bp = Blueprint('cli_bp', __name__)

@cli_bp.cli.command("create-db")
def create_db():
    """Tworzy wszystkie tabele w bazie danych."""
    db.create_all()
    click.echo("Baza danych i tabele zostały utworzone.")

@cli_bp.cli.command("drop-db")
def drop_db():
    """Usuwa wszystkie tabele z bazy danych."""
    db.drop_all()
    click.echo("Wszystkie tabele zostały usunięte z bazy danych.")

@cli_bp.cli.command("seed-db")
def seed_db():
    """Seedowanie bazy przykładowymi danymi."""
    # Dodaj reżyserów
    director1 = Director(name="Steven Spielberg")
    director2 = Director(name="Christopher Nolan")

    # Dodaj aktorów
    actor1 = Actor(name="Leonardo DiCaprio")
    actor2 = Actor(name="Tom Hanks")
    actor3 = Actor(name="Morgan Freeman")

    # Dodaj kategorie
    cat1 = Category(name="Drama")
    cat2 = Category(name="Sci-Fi")
    cat3 = Category(name="Comedy")

    # Dodaj filmy
    movie1 = Movie(title="Inception", release_year=2010, director=director2)
    movie1.actors.extend([actor1])
    movie1.categories.extend([cat2])

    movie2 = Movie(title="Saving Private Ryan", release_year=1998, director=director1)
    movie2.actors.extend([actor2])
    movie2.categories.extend([cat1])

    movie3 = Movie(title="Catch Me If You Can", release_year=2002, director=director1)
    movie3.actors.extend([actor2])
    movie3.categories.extend([cat1, cat3])

    # Dodaj recenzje
    review1 = Review(text="Bardzo dobry film!", rating=9, movie=movie1)
    review2 = Review(text="Trzyma w napięciu.", rating=8, movie=movie2)
    review3 = Review(text="Zabawny i wciągający.", rating=7, movie=movie3)

    db.session.add_all([director1, director2, actor1, actor2, actor3, cat1, cat2, cat3, movie1, movie2, movie3, review1, review2, review3])
    db.session.commit()
    click.echo("Baza danych została zapełniona przykładowymi danymi.")
