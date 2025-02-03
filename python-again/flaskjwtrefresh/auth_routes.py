from flask import Blueprint, request, jsonify, make_response
from database.db_connector import db
from models.user import User
from marshmallow import ValidationError
from schemas import RegisterSchema, LoginSchema
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required,
    set_access_cookies,
    set_refresh_cookies,
    unset_jwt_cookies
)

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

    new_user = User(username=validated_data["username"], email=validated_data["email"])
    new_user.set_password(validated_data["password"])

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully!"}), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    """Logowanie użytkownika i generowanie Access + Refresh Tokenów"""
    data = request.get_json()
    try:
        validated_data = LoginSchema().load(data)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    user = User.query.filter_by(email=validated_data["email"]).first()
    if not user or not user.check_password(validated_data["password"]):
        return jsonify({"error": "Invalid email or password"}), 401

    access_token = create_access_token(identity=str(user.id))
    refresh_token = create_refresh_token(identity=str(user.id))

    response = jsonify({
        "access_token": access_token,
        "refresh_token": refresh_token  # ✅ Teraz zwracamy Refresh Token w JSON
    })
    set_access_cookies(response, access_token)
    set_refresh_cookies(response, refresh_token)

    return response


@auth_bp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)  # ✅ Tylko Refresh Tokeny mogą tu działać
def refresh():
    """Odświeżanie Access Tokena za pomocą Refresh Tokena"""
    user_id = get_jwt_identity()
    access_token = create_access_token(identity=user_id)

    response = jsonify({"access_token": access_token})
    set_access_cookies(response, access_token)

    return response


@auth_bp.route("/logout", methods=["POST"])
def logout():
    """Wylogowanie - usunięcie tokenów"""
    response = jsonify({"message": "Successfully logged out"})
    unset_jwt_cookies(response)  # ✅ Usuwamy Refresh + Access Tokeny
    return response
