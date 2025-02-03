from database.db_connector import db

class User(db.Model):
    """Encja użytkownika (SQLAlchemy ORM)"""
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)

    def to_dict(self):
        """Konwertuje encję na JSON-serializable słownik"""
        return {"id": self.id, "username": self.username, "email": self.email}

    def __repr__(self):
        return f"User(id={self.id}, username='{self.username}', email='{self.email}')"