from flask import Flask
from database.db_connector import initialize_database
from api.user_routes import user_bp

app = Flask(__name__)

# Inicjalizacja bazy danych
initialize_database()

# Rejestracja blueprinta
app.register_blueprint(user_bp)

if __name__ == "__main__":
    app.run(debug=True)