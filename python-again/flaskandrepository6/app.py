import click
from flask import Flask
from flask_jwt_extended import JWTManager
from database.db_connector import init_db, db
from api.user_routes import user_bp
from api.auth_routes import auth_bp  # ✅ Import logowania JWT
from api.protected_routes import protected_bp  # ✅ Import zabezpieczonych endpointów

app = Flask(__name__)

# Konfiguracja JWT
app.config["JWT_SECRET_KEY"] = "super_secret_key"  # Klucz do podpisywania tokenów
jwt = JWTManager(app)

# Inicjalizacja bazy danych
init_db(app)

# Rejestracja Blueprintów
app.register_blueprint(user_bp)  # Obsługa użytkowników
app.register_blueprint(auth_bp)  # Logowanie JWT
app.register_blueprint(protected_bp)  # Endpointy wymagające JWT

# Tworzenie tabel przy pierwszym uruchomieniu
with app.app_context():
    db.create_all()

# Dodanie komendy `flask seed`
@app.cli.command("seed")
@click.argument("n", default=50, type=int)
def seed_command(n):
    """Generuje n fejkowych użytkowników."""
    from seed import seed_users  # ✅ Importujemy seed_users tutaj, a nie na początku!
    seed_users(n)

if __name__ == "__main__":
    app.run(debug=True)
