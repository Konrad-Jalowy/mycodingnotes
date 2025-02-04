from flask import Blueprint, request, jsonify
from app import db
from app.models import User, Group

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

# Tworzenie grupy
@main.route('/groups', methods=['POST'])
def create_group():
    data = request.json
    name = data.get('name')

    if not name:
        return jsonify({'error': 'No group name provided'}), 400

    group = Group(name=name)
    db.session.add(group)
    db.session.commit()

    return jsonify({'id': group.id, 'name': group.name})

# Dodawanie użytkownika do grupy
@main.route('/users/<int:user_id>/join/<int:group_id>', methods=['POST'])
def add_user_to_group(user_id, group_id):
    user = User.query.get(user_id)
    group = Group.query.get(group_id)

    if not user or not group:
        return jsonify({'error': 'User or group not found'}), 404

    if group in user.groups:
        return jsonify({'message': 'User is already in this group'}), 400

    user.groups.append(group)
    db.session.commit()

    return jsonify({'message': f'User {user.username} added to group {group.name}'})

# Pobranie grup użytkownika
@main.route('/users/<int:user_id>/groups', methods=['GET'])
def get_user_groups(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    groups = [{'id': group.id, 'name': group.name} for group in user.groups]
    return jsonify({'user': user.username, 'groups': groups})

# Pobranie użytkowników w grupie
@main.route('/groups/<int:group_id>/members', methods=['GET'])
def get_group_members(group_id):
    group = Group.query.get(group_id)
    if not group:
        return jsonify({'error': 'Group not found'}), 404

    members = [{'id': user.id, 'username': user.username} for user in group.members]
    return jsonify({'group': group.name, 'members': members})
