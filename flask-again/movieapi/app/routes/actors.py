from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import Actor

actors_bp = Blueprint('actors_bp', __name__)

@actors_bp.route("/", methods=["GET"])
def get_actors():
    actors = Actor.query.all()
    results = []
    for actor in actors:
        results.append({"id": actor.id, "name": actor.name})
    return jsonify(results), 200

@actors_bp.route("/", methods=["POST"])
def create_actor():
    data = request.get_json()
    name = data.get("name")
    actor = Actor(name=name)
    db.session.add(actor)
    db.session.commit()
    return jsonify({"message": "Actor created", "actor_id": actor.id}), 201

@actors_bp.route("/<int:actor_id>", methods=["GET"])
def get_actor(actor_id):
    actor = Actor.query.get_or_404(actor_id)
    return jsonify({"id": actor.id, "name": actor.name}), 200

@actors_bp.route("/<int:actor_id>", methods=["PUT", "PATCH"])
def update_actor(actor_id):
    actor = Actor.query.get_or_404(actor_id)
    data = request.get_json()
    actor.name = data.get("name", actor.name)
    db.session.commit()
    return jsonify({"message": "Actor updated"}), 200

@actors_bp.route("/<int:actor_id>", methods=["DELETE"])
def delete_actor(actor_id):
    actor = Actor.query.get_or_404(actor_id)
    db.session.delete(actor)
    db.session.commit()
    return jsonify({"message": "Actor deleted"}), 200
