from flask import Blueprint, request, jsonify
from app import db
from app.models import User, Note

main = Blueprint('main', __name__)

# Tworzenie użytkownika
@main.route('/users', methods=['POST'])
def create_user():
    data = request.json
    username = data.get('username')

    if not username:
        return jsonify({'error': 'No username provided'}), 400

    user = User(username=username)
    db.session.add(user)
    db.session.commit()

    return jsonify({'id': user.id, 'username': user.username})

# Tworzenie notatki dla użytkownika
@main.route('/users/<int:user_id>/notes', methods=['POST'])
def create_note(user_id):
    data = request.json
    content = data.get('content')

    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    note = Note(content=content, user_id=user_id)
    db.session.add(note)
    db.session.commit()

    return jsonify({'id': note.id, 'content': note.content, 'user_id': note.user_id})

# Pobranie wszystkich notatek użytkownika
@main.route('/users/<int:user_id>/notes', methods=['GET'])
def get_user_notes(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    notes = [{'id': note.id, 'content': note.content} for note in user.notes]
    return jsonify({'user': user.username, 'notes': notes})
