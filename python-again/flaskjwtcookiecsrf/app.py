from flask import Flask
from database.db_connector import init_db, db
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "super_secret_key"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 900  # 15 minut
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = 604800  # 7 dni
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]  # Tokeny w Cookies
app.config["JWT_COOKIE_CSRF_PROTECT"] = True  # Wymagamy CSRF Tokena dla Refresh Tokenów
app.config["JWT_COOKIE_SECURE"] = False  # W produkcji ustaw na True (HTTPS wymagane)

init_db(app)
jwt = JWTManager(app)

from routes.auth_routes import auth_bp
from routes.protected_routes import protected_bp

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(protected_bp, url_prefix="/api")

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
