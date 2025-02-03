from flask import Blueprint, request, jsonify
from database.db_connector import db
from models.user import User
from marshmallow import ValidationError
from schemas import RegisterSchema, LoginSchema
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    """Rejestracja nowego użytkownika"""
    data = request.get_json()

    try:
        validated_data = RegisterSchema().load(data)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    if User.query.filter_by(email=validated_data["email"]).first():
        return jsonify({"error": "Email already registered"}), 400

    new_user = User(
        username=validated_data["username"],
        email=validated_data["email"]
    )
    new_user.set_password(validated_data["password"])  # Haszowanie hasła

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully!"}), 201
@auth_bp.route("/login", methods=["POST"])
def login():
    """Logowanie użytkownika i generowanie JWT"""
    data = request.get_json()

    try:
        validated_data = LoginSchema().load(data)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    user = User.query.filter_by(email=validated_data["email"]).first()
    if not user or not user.check_password(validated_data["password"]):
        return jsonify({"error": "Invalid email or password"}), 401

    access_token = create_access_token(identity=str(user.id))  # ✅ Zamiana ID na string
    return jsonify({"access_token": access_token})
