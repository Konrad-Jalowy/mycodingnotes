from flask import Blueprint, request, jsonify
from repositories.user_repository import UserRepository
from models.user import User

user_repo = UserRepository()
user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/users", methods=["GET"])
def get_all_users():
    """Pobiera wszystkich użytkowników."""
    users = user_repo.get_all_users()
    return jsonify([user.__dict__ for user in users])  # Konwersja do JSON

@user_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    """Pobiera użytkownika po ID."""
    user = user_repo.get_user_by_id(user_id)
    return jsonify(user.__dict__) if user else (jsonify({"error": "User not found"}), 404)

@user_bp.route("/users", methods=["POST"])
def create_user():
    """Dodaje nowego użytkownika."""
    data = request.get_json()
    if "username" not in data or "email" not in data:
        return jsonify({"error": "Missing fields"}), 400

    new_user = user_repo.add_user(User(username=data["username"], email=data["email"]))
    return jsonify(new_user.__dict__), 201

@user_bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    """Usuwa użytkownika po ID."""
    affected_rows = user_repo.delete_user(user_id)
    if affected_rows > 0:
        return jsonify({"message": "User deleted"}), 200
    return jsonify({"error": "User not found"}), 404