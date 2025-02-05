from flask import Flask
from config import Config
from app.extensions import db
from app.routes.actors import actors_bp
from app.routes.categories import categories_bp
from app.routes.directors import directors_bp
from app.routes.movies import movies_bp
from app.routes.reviews import reviews_bp
from app.cli import cli_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Rejestracja blueprintów routes
    app.register_blueprint(movies_bp, url_prefix="/movies")
    app.register_blueprint(actors_bp, url_prefix="/actors")
    app.register_blueprint(directors_bp, url_prefix="/directors")
    app.register_blueprint(reviews_bp, url_prefix="/reviews")
    app.register_blueprint(categories_bp, url_prefix="/categories")

    # Rejestracja blueprintu CLI (komendy create-db, drop-db, seed-db)
    app.register_blueprint(cli_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()
