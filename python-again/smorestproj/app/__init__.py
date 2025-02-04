from flask import Flask
from flask_smorest import Api
from app.models import db
from app.routes import blp as UserBlueprint

def create_app():
    app = Flask(__name__)

    # ✅ KONFIGURACJA OPENAPI DLA FLASK-SMOREST
    app.config["API_TITLE"] = "Flask-Smorest API"  # 📌 Nazwa API (WYMAGANE)
    app.config["API_VERSION"] = "v1"  # 📌 Wersja API
    app.config["OPENAPI_VERSION"] = "3.0.2"  # 📌 Wersja OpenAPI
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/docs"  # 📌 Ścieżka do Swagger UI
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.52.5/"  # 📌 Link do Swagger UI

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    api = Api(app)
    api.register_blueprint(UserBlueprint)  # ✅ Rejestracja naszego API

    with app.app_context():
        db.create_all()

    return app
