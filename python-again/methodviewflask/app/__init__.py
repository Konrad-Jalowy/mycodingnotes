from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from app.routes import register_routes
    register_routes(app)  # Rejestrujemy nasze API

    with app.app_context():
        db.create_all()  # Tworzy tabelę, jeśli nie istnieje

    return app
