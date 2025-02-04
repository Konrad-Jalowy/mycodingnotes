from flask_restful import Resource, reqparse
from app.models import Group
from app import db

group_parser = reqparse.RequestParser()
group_parser.add_argument("name", type=str, required=True, help="Group name is required", location="json")

class GroupListResource(Resource):
    def get(self):
        """ Pobiera listę grup """
        groups = Group.query.all()
        return [{"id": group.id, "name": group.name} for group in groups]

    def post(self):
        """ Dodaje nową grupę """
        args = group_parser.parse_args()
        if Group.query.filter_by(name=args["name"]).first():
            return {"error": "Group already exists"}, 409
        group = Group(name=args["name"])
        db.session.add(group)
        db.session.commit()
        return {"id": group.id, "name": group.name}, 201

class GroupResource(Resource):
    def get(self, group_id):
        """ Pobiera grupę po ID """
        group = Group.query.get(group_id)
        if not group:
            return {"error": "Group not found"}, 404
        return {"id": group.id, "name": group.name}

    def delete(self, group_id):
        """ Usuwa grupę """
        group = Group.query.get(group_id)
        if not group:
            return {"error": "Group not found"}, 404
        db.session.delete(group)
        db.session.commit()
        return {"message": "Group deleted"}, 200
