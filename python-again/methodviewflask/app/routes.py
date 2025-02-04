from flask import request, jsonify
from flask.views import MethodView
from app.models import db, User


class UserView(MethodView):
    def get(self, user_id=None):
        """ Pobiera listę użytkowników lub jednego użytkownika """
        if user_id:
            user = User.query.get_or_404(user_id)
            return jsonify({"id": user.id, "username": user.username})

        users = User.query.all()
        return jsonify([{"id": u.id, "username": u.username} for u in users])

    def post(self):
        """ Tworzy nowego użytkownika """
        data = request.json
        if not data or "username" not in data:
            return jsonify({"error": "Username is required"}), 400

        if User.query.filter_by(username=data["username"]).first():
            return jsonify({"error": "Username already exists"}), 409

        user = User(username=data["username"])
        db.session.add(user)
        db.session.commit()
        return jsonify({"id": user.id, "username": user.username}), 201

    def delete(self, user_id):
        """ Usuwa użytkownika """
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted"}), 200


def register_routes(app):
    user_view = UserView.as_view("user_api")

    app.add_url_rule("/users", view_func=user_view, methods=["GET", "POST"])  # 🔹 Usunięto `defaults={"user_id": None}`
    app.add_url_rule("/users/<int:user_id>", view_func=user_view, methods=["GET", "DELETE"])
