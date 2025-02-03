from flask import Flask
from database.db_connector import init_db, db
from flask_jwt_extended import JWTManager

app = Flask(__name__)

# Inicjalizacja bazy danych
init_db(app)

app.config["JWT_SECRET_KEY"] = "super_secret_key"  # Klucz JWT
jwt = JWTManager(app)

# Importujemy i rejestrujemy Blueprints
from routes.auth_routes import auth_bp
from routes.protected_routes import protected_bp

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(protected_bp, url_prefix="/api")

# Tworzymy bazę
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
