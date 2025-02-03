from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.user import User

protected_bp = Blueprint("protected_bp", __name__)


@protected_bp.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    """Zabezpieczona trasa dostępna tylko po zalogowaniu"""
    user_id = get_jwt_identity()  # Pobieramy ID z tokena (jest stringiem!)

    # Konwertujemy user_id na int, bo w bazie mamy liczby
    user = User.query.get(int(user_id))  # ✅ Zamieniamy na int przed szukaniem w bazie

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify({"message": f"Hello, {user.username}!", "user": user.to_dict()})