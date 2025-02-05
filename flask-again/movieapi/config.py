import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    DEBUG = True
    # Ścieżka do bazy SQLite w pliku movie_api.db w katalogu głównym projektu
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'movie_api.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Możesz dodać dowolne dodatkowe konfiguracje
