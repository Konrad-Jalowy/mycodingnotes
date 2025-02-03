from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth_bp", __name__)

# Proste logowanie (bez haseł, bo nie mamy jeszcze autoryzacji)
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Generujemy JWT dla użytkownika
    access_token = create_access_token(identity=username)
    return jsonify({"access_token": access_token})