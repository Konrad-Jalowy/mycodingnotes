from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Tworzymy obiekt SQLAlchemy
db = SQLAlchemy()

def create_app():
    print("🔹 create_app() uruchomione!")  # Debugging

    app = Flask(__name__)

    # Konfiguracja bazy danych (sqlite w katalogu głównym)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shortener.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    print("SQLALCHEMY_DATABASE_URI:", app.config.get("SQLALCHEMY_DATABASE_URI"))  # Debugging

    db.init_app(app)  # Inicjalizacja bazy danych

    from app.routes import main
    app.register_blueprint(main)  # Rejestracja blueprintów

    with app.app_context():
        db.create_all()  # Tworzenie tabel w bazie

    return app
