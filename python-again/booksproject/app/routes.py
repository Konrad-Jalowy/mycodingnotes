# app/routes.py
from flask import Blueprint, request, jsonify
from .database import db
from .models import Author, Book

api = Blueprint('api', __name__)

@api.route('/authors', methods=['GET'])
def get_authors():
    authors = Author.query.all()
    return jsonify([author.to_dict() for author in authors]), 200

@api.route('/authors/<int:author_id>', methods=['GET'])
def get_author(author_id):
    author = Author.query.get_or_404(author_id)
    return jsonify(author.to_dict()), 200

@api.route('/authors', methods=['POST'])
def create_author():
    data = request.get_json()
    new_author = Author(name=data['name'])
    db.session.add(new_author)
    db.session.commit()
    return jsonify(new_author.to_dict()), 201

@api.route('/authors/<int:author_id>', methods=['PUT'])
def update_author(author_id):
    author = Author.query.get_or_404(author_id)
    data = request.get_json()
    author.name = data.get('name', author.name)
    db.session.commit()
    return jsonify(author.to_dict()), 200

@api.route('/authors/<int:author_id>', methods=['DELETE'])
def delete_author(author_id):
    author = Author.query.get_or_404(author_id)
    db.session.delete(author)
    db.session.commit()
    return jsonify({"message": "Author deleted"}), 200


@api.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books]), 200

@api.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    new_book = Book(
        title=data['title'],
        author_id=data['author_id']
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.to_dict()), 201

