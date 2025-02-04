from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    api = Api(app)

    from app.resources import UserResource, UserListResource, GroupResource, GroupListResource, UserGroupResource

    # Rejestrujemy endpointy
    api.add_resource(UserListResource, '/users')
    api.add_resource(UserResource, '/users/<int:user_id>')
    api.add_resource(GroupListResource, '/groups')
    api.add_resource(GroupResource, '/groups/<int:group_id>')
    api.add_resource(UserGroupResource, '/users/<int:user_id>/join/<int:group_id>')

    with app.app_context():
        db.create_all()

    return app
