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

if __name__ == "__main__":
    app.run(debug=True)
