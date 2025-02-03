from flask import Blueprint, request, jsonify
from repositories.user_repository import UserRepository

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/users", methods=["GET"])
def get_all_users():
    """Pobiera wszystkich użytkowników"""
    users = UserRepository.get_all_users()
    return jsonify([user.to_dict() for user in users])

@user_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    """Pobiera użytkownika po ID"""
    user = UserRepository.get_user_by_id(user_id)
    return jsonify(user.to_dict()) if user else (jsonify({"error": "User not found"}), 404)

@user_bp.route("/users", methods=["POST"])
def create_user():
    """Dodaje nowego użytkownika"""
    data = request.get_json()
    if "username" not in data or "email" not in data:
        return jsonify({"error": "Missing fields"}), 400

    new_user = UserRepository.add_user(data["username"], data["email"])
    return jsonify(new_user.to_dict()), 201

@user_bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    """Usuwa użytkownika po ID"""
    success = UserRepository.delete_user(user_id)
    return jsonify({"message": "User deleted"}) if success else (jsonify({"error": "User not found"}), 404)
