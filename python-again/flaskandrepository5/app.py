import click
from flask import Flask
from database.db_connector import init_db, db
from api.user_routes import user_bp

app = Flask(__name__)

# Inicjalizacja bazy danych
init_db(app)
app.register_blueprint(user_bp)

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
