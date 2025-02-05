from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import Director

directors_bp = Blueprint('directors_bp', __name__)

@directors_bp.route("/", methods=["GET"])
def get_directors():
    directors = Director.query.all()
    results = []
    for director in directors:
        results.append({"id": director.id, "name": director.name})
    return jsonify(results), 200

@directors_bp.route("/", methods=["POST"])
def create_director():
    data = request.get_json()
    name = data.get("name")
    director = Director(name=name)
    db.session.add(director)
    db.session.commit()
    return jsonify({"message": "Director created", "director_id": director.id}), 201

@directors_bp.route("/<int:director_id>", methods=["GET"])
def get_director(director_id):
    director = Director.query.get_or_404(director_id)
    return jsonify({"id": director.id, "name": director.name}), 200

@directors_bp.route("/<int:director_id>", methods=["PUT", "PATCH"])
def update_director(director_id):
    director = Director.query.get_or_404(director_id)
    data = request.get_json()
    director.name = data.get("name", director.name)
    db.session.commit()
    return jsonify({"message": "Director updated"}), 200

@directors_bp.route("/<int:director_id>", methods=["DELETE"])
def delete_director(director_id):
    director = Director.query.get_or_404(director_id)
    db.session.delete(director)
    db.session.commit()
    return jsonify({"message": "Director deleted"}), 200