from flask_smorest import Blueprint
from flask.views import MethodView
from app.models import db, User
from app.schemas import UserSchema

blp = Blueprint("users", __name__, description="User management")

@blp.route("/users")
class UserList(MethodView):  # ✅ Dodaj `MethodView`
    @blp.response(200, UserSchema(many=True))
    def get(self):
        """ Pobiera listę użytkowników """
        return User.query.all()

    @blp.arguments(UserSchema)
    @blp.response(201, UserSchema)
    def post(self, user_data):
        """ Tworzy użytkownika """
        user = User(username=user_data["username"])
        db.session.add(user)
        db.session.commit()
        return user

@blp.route("/users/<int:user_id>")
class UserResource(MethodView):  # ✅ Dodaj `MethodView`
    @blp.response(200, UserSchema)
    def get(self, user_id):
        """ Pobiera użytkownika po ID """
        user = User.query.get_or_404(user_id)
        return user

    @blp.response(204)
    def delete(self, user_id):
        """ Usuwa użytkownika """
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return ""

