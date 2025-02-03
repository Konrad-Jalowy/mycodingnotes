from flask import Blueprint, request, jsonify
from repositories.user_repository import UserRepository

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/users", methods=["GET"])
def get_all_users():
    """Pobiera wszystkich użytkowników z filtrowaniem i paginacją"""
    username = request.args.get("username")  # Pobiera username z URL
    email = request.args.get("email")  # Pobiera email z URL
    page = request.args.get("page", default=1, type=int)  # Pobiera numer strony
    limit = request.args.get("limit", default=10, type=int)  # Pobiera limit użytkowników

    users, total = UserRepository.get_all_users(username=username, email=email, page=page, limit=limit)

    return jsonify({
        "total_users": total,
        "page": page,
        "limit": limit,
        "users": [user.to_dict() for user in users]
    })



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