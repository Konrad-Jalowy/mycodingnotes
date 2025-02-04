from flask import Blueprint, request, jsonify
from datetime import datetime
from app import db
from app.models import User, Group, user_group

main = Blueprint('main', __name__)

@main.route('/users', methods=['POST'])
def create_user():
    data = request.json
    username = data.get('username')

    if not username:
        return jsonify({'error': 'No username provided'}), 400

    # SPRAWDZENIE, CZY UŻYTKOWNIK JUŻ ISTNIEJE
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'error': 'Username already exists'}), 409  # 409 Conflict

    user = User(username=username)
    db.session.add(user)
    db.session.commit()

    return jsonify({'id': user.id, 'username': user.username}), 201  # 201 Created

@main.route('/groups', methods=['POST'])
def create_group():
    data = request.json
    name = data.get('name')

    if not name:
        return jsonify({'error': 'No group name provided'}), 400

    # Sprawdzamy, czy taka grupa już istnieje
    existing_group = Group.query.filter_by(name=name).first()
    if existing_group:
        return jsonify({'error': 'Group name already exists'}), 409  # Conflict

    group = Group(name=name)
    db.session.add(group)
    db.session.commit()

    return jsonify({'id': group.id, 'name': group.name}), 201  # 201 Created


# Dodawanie użytkownika do grupy z zapisem daty
@main.route('/users/<int:user_id>/join/<int:group_id>', methods=['POST'])
def add_user_to_group(user_id, group_id):
    user = User.query.get(user_id)
    group = Group.query.get(group_id)

    if not user or not group:
        return jsonify({'error': 'User or group not found'}), 404

    # Sprawdzenie, czy użytkownik już jest w grupie
    existing_entry = db.session.execute(
        user_group.select().where(
            (user_group.c.user_id == user_id) & (user_group.c.group_id == group_id)
        )
    ).fetchone()

    if existing_entry:
        return jsonify({'message': 'User is already in this group'}), 400

    # Dodanie użytkownika do grupy z datą dołączenia
    stmt = user_group.insert().values(user_id=user_id, group_id=group_id, joined_at=datetime.utcnow())
    db.session.execute(stmt)
    db.session.commit()

    return jsonify({'message': f'User {user.username} added to group {group.name}'})


# Pobranie grup użytkownika + daty dołączenia
@main.route('/users/<int:user_id>/groups', methods=['GET'])
def get_user_groups(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    # Pobieramy grupy i datę dołączenia
    groups = db.session.execute(
        user_group.select().where(user_group.c.user_id == user_id)
    ).fetchall()

    groups_data = []
    for g in groups:
        group = Group.query.get(g.group_id)
        groups_data.append({
            'id': group.id,
            'name': group.name,
            'joined_at': g.joined_at.strftime('%Y-%m-%d %H:%M:%S')  # Formatowanie daty
        })

    return jsonify({'user': user.username, 'groups': groups_data})


# Pobranie użytkowników w grupie + daty dołączenia
@main.route('/groups/<int:group_id>/members', methods=['GET'])
def get_group_members(group_id):
    group = Group.query.get(group_id)
    if not group:
        return jsonify({'error': 'Group not found'}), 404

    # Pobieramy użytkowników i ich datę dołączenia
    members = db.session.execute(
        user_group.select().where(user_group.c.group_id == group_id)
    ).fetchall()

    members_data = []
    for m in members:
        user = User.query.get(m.user_id)
        members_data.append({
            'id': user.id,
            'username': user.username,
            'joined_at': m.joined_at.strftime('%Y-%m-%d %H:%M:%S')  # Formatowanie daty
        })

    return jsonify({'group': group.name, 'members': members_data})


# Usuwanie użytkownika z grupy
@main.route('/users/<int:user_id>/leave/<int:group_id>', methods=['DELETE'])
def remove_user_from_group(user_id, group_id):
    user = User.query.get(user_id)
    group = Group.query.get(group_id)

    if not user or not group:
        return jsonify({'error': 'User or group not found'}), 404

    # Sprawdzenie, czy użytkownik jest w grupie
    existing_entry = db.session.execute(
        user_group.select().where(
            (user_group.c.user_id == user_id) & (user_group.c.group_id == group_id)
        )
    ).fetchone()

    if not existing_entry:
        return jsonify({'message': 'User is not in this group'}), 400

    # Usunięcie użytkownika z grupy
    stmt = user_group.delete().where(
        (user_group.c.user_id == user_id) & (user_group.c.group_id == group_id)
    )
    db.session.execute(stmt)
    db.session.commit()

    return jsonify({'message': f'User {user.username} removed from group {group.name}'})
