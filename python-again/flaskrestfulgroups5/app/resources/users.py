from flask_restful import Resource, reqparse
from app.models import User
from app import db

# Parser dla GET (paginacja)
user_list_parser = reqparse.RequestParser()
user_list_parser.add_argument("page", type=int, default=1, location="args")
user_list_parser.add_argument("per_page", type=int, default=5, location="args")

# Parser dla POST (dodanie użytkownika)
user_create_parser = reqparse.RequestParser()
user_create_parser.add_argument("username", type=str, required=True, help="Username is required", location="json")

class UserListResource(Resource):
    def get(self):
        """ Pobiera użytkowników z paginacją """
        args = user_list_parser.parse_args()
        pagination = User.query.paginate(page=args["page"], per_page=args["per_page"])
        return {
            "total_users": pagination.total,
            "total_pages": pagination.pages,
            "current_page": pagination.page,
            "per_page": pagination.per_page,
            "users": [{"id": user.id, "username": user.username} for user in pagination.items]
        }

    def post(self):
        """ Dodaje nowego użytkownika """
        args = user_create_parser.parse_args()
        if User.query.filter_by(username=args["username"]).first():
            return {"error": "Username already exists"}, 409
        user = User(username=args["username"])
        db.session.add(user)
        db.session.commit()
        return {"id": user.id, "username": user.username}, 201

class UserResource(Resource):
    def get(self, user_id):
        """ Pobiera użytkownika po ID """
        user = User.query.get(user_id)
        if not user:
            return {"error": "User not found"}, 404
        return {"id": user.id, "username": user.username}

    def delete(self, user_id):
        """ Usuwa użytkownika """
        user = User.query.get(user_id)
        if not user:
            return {"error": "User not found"}, 404
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted"}, 200
