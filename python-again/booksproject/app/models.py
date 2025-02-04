# app/models.py
from .database import db

class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)

    # Relacja do Book
    books = db.relationship('Book', backref='author', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author_id": self.author_id
        }
