from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

protected_bp = Blueprint("protected_bp", __name__)

@protected_bp.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    """Endpoint wymagający autoryzacji JWT"""
    current_user = get_jwt_identity()  # Pobieramy tożsamość użytkownika z tokena
    return jsonify({"message": f"Hello, {current_user}! This is a protected route."})
