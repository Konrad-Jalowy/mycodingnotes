from app.extensions import db

# Tabela łącznikowa Film-Aktor (wielu aktorów gra w wielu filmach)
movie_actor = db.Table(
    'movie_actor',
    db.Column('movie_id', db.Integer, db.ForeignKey('movies.id')),
    db.Column('actor_id', db.Integer, db.ForeignKey('actors.id'))
)

# Tabela łącznikowa Film-Kategoria (wiele kategorii przypada na jeden film i odwrotnie)
movie_category = db.Table(
    'movie_category',
    db.Column('movie_id', db.Integer, db.ForeignKey('movies.id')),
    db.Column('category_id', db.Integer, db.ForeignKey('categories.id'))
)

class Movie(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    release_year = db.Column(db.Integer, nullable=True)

    # Relacja do reżysera (jeden reżyser może mieć wiele filmów)
    director_id = db.Column(db.Integer, db.ForeignKey('directors.id'), nullable=True)
    director = db.relationship("Director", back_populates="movies")

    # Relacja do aktorów (wielu aktorów -> wiele filmów)
    actors = db.relationship("Actor", secondary=movie_actor, back_populates="movies")

    # Relacja do kategorii (wiele kategorii -> wiele filmów)
    categories = db.relationship("Category", secondary=movie_category, back_populates="movies")

    # Relacja do recenzji (jeden film -> wiele recenzji)
    reviews = db.relationship("Review", back_populates="movie", cascade="all, delete-orphan")


class Actor(db.Model):
    __tablename__ = "actors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    # Relacja do filmów
    movies = db.relationship("Movie", secondary=movie_actor, back_populates="actors")


class Director(db.Model):
    __tablename__ = "directors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    # Relacja odwrotna (list of movies)
    movies = db.relationship("Movie", back_populates="director")


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    # Relacja do filmów
    movies = db.relationship("Movie", secondary=movie_category, back_populates="categories")


class Review(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    # Relacja do filmu
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False)
    movie = db.relationship("Movie", back_populates="reviews")
