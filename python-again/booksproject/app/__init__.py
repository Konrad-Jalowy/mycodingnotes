# app/__init__.py
from flask import Flask
from config import Config
from .database import db
from .routes import api


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Rejestrowanie blueprintu
    app.register_blueprint(api, url_prefix='/api')

    # Tworzenie tabel, jeśli nie istnieją
    with app.app_context():
        db.create_all()

    return app
