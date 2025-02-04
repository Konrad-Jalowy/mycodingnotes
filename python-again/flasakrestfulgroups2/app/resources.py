from flask_restful import Resource, reqparse
from app import db
from app.models import User, Group

# Parser do pobierania JSON-a z requesta
user_parser = reqparse.RequestParser()
user_parser.add_argument("username", type=str, required=True, help="Username is required")

group_parser = reqparse.RequestParser()
group_parser.add_argument("name", type=str, required=True, help="Group name is required")

# CRUD dla użytkowników
from flask_restful import Resource, reqparse
from app import db
from app.models import User, Group

# Parser do aktualizacji użytkownika
update_user_parser = reqparse.RequestParser()
update_user_parser.add_argument("username", type=str, required=True, help="New username is required")


class UserResource(Resource):
    def get(self, user_id):
        """ Pobiera użytkownika po ID """
        user = User.query.get(user_id)
        if not user:
            return {"error": "User not found"}, 404
        return {"id": user.id, "username": user.username}

    def put(self, user_id):
        """ Aktualizuje użytkownika """
        user = User.query.get(user_id)
        if not user:
            return {"error": "User not found"}, 404

        args = update_user_parser.parse_args()

        # Sprawdzamy, czy nowa nazwa użytkownika już istnieje
        if User.query.filter_by(username=args["username"]).first():
            return {"error": "Username already exists"}, 409

        user.username = args["username"]
        db.session.commit()
        return {"id": user.id, "username": user.username}, 200

    def delete(self, user_id):
        """ Usuwa użytkownika """
        user = User.query.get(user_id)
        if not user:
            return {"error": "User not found"}, 404
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted"}, 200


class UserListResource(Resource):
    def get(self):
        users = User.query.all()
        return [{"id": user.id, "username": user.username} for user in users]

    def post(self):
        args = user_parser.parse_args()
        if User.query.filter_by(username=args["username"]).first():
            return {"error": "Username already exists"}, 409
        user = User(username=args["username"])
        db.session.add(user)
        db.session.commit()
        return {"id": user.id, "username": user.username}, 201

# Parser do aktualizacji grupy


update_group_parser = reqparse.RequestParser()
update_group_parser.add_argument("name", type=str, required=True, help="New group name is required")

class GroupResource(Resource):
    def get(self, group_id):
        """ Pobiera grupę po ID """
        group = Group.query.get(group_id)
        if not group:
            return {"error": "Group not found"}, 404
        return {"id": group.id, "name": group.name}

    def put(self, group_id):
        """ Aktualizuje grupę """
        group = Group.query.get(group_id)
        if not group:
            return {"error": "Group not found"}, 404

        args = update_group_parser.parse_args()

        # Sprawdzamy, czy nowa nazwa grupy już istnieje
        if Group.query.filter_by(name=args["name"]).first():
            return {"error": "Group name already exists"}, 409

        group.name = args["name"]
        db.session.commit()
        return {"id": group.id, "name": group.name}, 200

    def delete(self, group_id):
        """ Usuwa grupę """
        group = Group.query.get(group_id)
        if not group:
            return {"error": "Group not found"}, 404
        db.session.delete(group)
        db.session.commit()
        return {"message": "Group deleted"}, 200

class GroupListResource(Resource):
    def get(self):
        groups = Group.query.all()
        return [{"id": group.id, "name": group.name} for group in groups]

    def post(self):
        args = group_parser.parse_args()
        if Group.query.filter_by(name=args["name"]).first():
            return {"error": "Group already exists"}, 409
        group = Group(name=args["name"])
        db.session.add(group)
        db.session.commit()
        return {"id": group.id, "name": group.name}, 201

# Przypisywanie użytkownika do grupy
class UserGroupResource(Resource):
    def post(self, user_id, group_id):
        user = User.query.get(user_id)
        group = Group.query.get(group_id)

        if not user or not group:
            return {"error": "User or Group not found"}, 404

        if group in user.groups:
            return {"message": "User is already in this group"}, 400

        user.groups.append(group)
        db.session.commit()
        return {"message": f"User {user.username} added to group {group.name}"}, 201
