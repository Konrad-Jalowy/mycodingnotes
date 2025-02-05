from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import Movie, Actor, Director, Category

movies_bp = Blueprint('movies_bp', __name__)

@movies_bp.route("/", methods=["GET"])
def get_movies():
    """
    Obsługa filtrowania:
    - /movies?actor=John
    - /movies?director=Spielberg
    - /movies?category=Comedy
    - /movies?page=1&per_page=10
    """
    query = Movie.query

    actor_name = request.args.get("actor")
    if actor_name:
        query = query.join(Movie.actors).filter(Actor.name.ilike(f"%{actor_name}%"))

    director_name = request.args.get("director")
    if director_name:
        query = query.join(Movie.director).filter(Director.name.ilike(f"%{director_name}%"))

    category_name = request.args.get("category")
    if category_name:
        query = query.join(Movie.categories).filter(Category.name.ilike(f"%{category_name}%"))

    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)
    pagination = query.paginate(page=page, per_page=per_page, error_out=False)
    movies = pagination.items

    results = []
    for movie in movies:
        results.append({
            "id": movie.id,
            "title": movie.title,
            "release_year": movie.release_year,
            "director": movie.director.name if movie.director else None,
            "actors": [actor.name for actor in movie.actors],
            "categories": [cat.name for cat in movie.categories]
        })

    return jsonify({
        "total": pagination.total,
        "page": pagination.page,
        "pages": pagination.pages,
        "per_page": pagination.per_page,
        "movies": results
    }), 200


@movies_bp.route("/", methods=["POST"])
def create_movie():
    data = request.get_json()
    title = data.get("title")
    release_year = data.get("release_year")
    director_id = data.get("director_id")
    actor_ids = data.get("actor_ids", [])
    category_ids = data.get("category_ids", [])

    movie = Movie(title=title, release_year=release_year)

    if director_id:
        director = Director.query.get(director_id)
        if director:
            movie.director = director

    if actor_ids:
        actors = Actor.query.filter(Actor.id.in_(actor_ids)).all()
        movie.actors.extend(actors)

    if category_ids:
        categories = Category.query.filter(Category.id.in_(category_ids)).all()
        movie.categories.extend(categories)

    db.session.add(movie)
    db.session.commit()

    return jsonify({"message": "Movie created", "movie_id": movie.id}), 201


@movies_bp.route("/<int:movie_id>", methods=["GET"])
def get_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    data = {
        "id": movie.id,
        "title": movie.title,
        "release_year": movie.release_year,
        "director": movie.director.name if movie.director else None,
        "actors": [actor.name for actor in movie.actors],
        "categories": [cat.name for cat in movie.categories]
    }
    return jsonify(data), 200


@movies_bp.route("/<int:movie_id>", methods=["PUT", "PATCH"])
def update_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    data = request.get_json()

    movie.title = data.get("title", movie.title)
    movie.release_year = data.get("release_year", movie.release_year)

    # Zaktualizuj reżysera (opcjonalnie)
    director_id = data.get("director_id")
    if director_id is not None:
        director = Director.query.get(director_id)
        if director:
            movie.director = director

    # Zaktualizuj aktorów (jeśli podano actor_ids)
    actor_ids = data.get("actor_ids")
    if actor_ids is not None:
        # Wyczyść aktualną listę
        movie.actors.clear()
        actors = Actor.query.filter(Actor.id.in_(actor_ids)).all()
        movie.actors.extend(actors)

    # Zaktualizuj kategorie (jeśli podano category_ids)
    category_ids = data.get("category_ids")
    if category_ids is not None:
        # Wyczyść aktualną listę
        movie.categories.clear()
        categories = Category.query.filter(Category.id.in_(category_ids)).all()
        movie.categories.extend(categories)

    db.session.commit()
    return jsonify({"message": "Movie updated"}), 200


@movies_bp.route("/<int:movie_id>", methods=["DELETE"])
def delete_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return jsonify({"message": "Movie deleted"}), 200