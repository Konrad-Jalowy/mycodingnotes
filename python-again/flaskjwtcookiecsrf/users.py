from database.db_connector import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    """Model użytkownika"""
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

    def set_password(self, password):
        """Haszuje hasło i zapisuje je w bazie"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Sprawdza poprawność hasła"""
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {"id": self.id, "username": self.username, "email": self.email}
