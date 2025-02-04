from flask_restful import Resource, reqparse
from app import db
from app.models import User, Group

# Parser do pobierania JSON-a z requesta
user_parser = reqparse.RequestParser()
user_parser.add_argument("username", type=str, required=True, help="Username is required")

group_parser = reqparse.RequestParser()
group_parser.add_argument("name", type=str, required=True, help="Group name is required")

# CRUD dla użytkowników
class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {"error": "User not found"}, 404
        return {"id": user.id, "username": user.username}

    def delete(self, user_id):
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

# CRUD dla grup
class GroupResource(Resource):
    def get(self, group_id):
        group = Group.query.get(group_id)
        if not group:
            return {"error": "Group not found"}, 404
        return {"id": group.id, "name": group.name}

    def delete(self, group_id):
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