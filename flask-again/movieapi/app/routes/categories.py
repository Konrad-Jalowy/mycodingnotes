from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import Category

categories_bp = Blueprint('categories_bp', __name__)

@categories_bp.route("/", methods=["GET"])
def get_categories():
    categories = Category.query.all()
    results = []
    for category in categories:
        results.append({"id": category.id, "name": category.name})
    return jsonify(results), 200

@categories_bp.route("/", methods=["POST"])
def create_category():
    data = request.get_json()
    name = data.get("name")
    category = Category(name=name)
    db.session.add(category)
    db.session.commit()
    return jsonify({"message": "Category created", "category_id": category.id}), 201

@categories_bp.route("/<int:category_id>", methods=["GET"])
def get_category(category_id):
    category = Category.query.get_or_404(category_id)
    return jsonify({"id": category.id, "name": category.name}), 200

@categories_bp.route("/<int:category_id>", methods=["PUT", "PATCH"])
def update_category(category_id):
    category = Category.query.get_or_404(category_id)
    data = request.get_json()
    category.name = data.get("name", category.name)
    db.session.commit()
    return jsonify({"message": "Category updated"}), 200

@categories_bp.route("/<int:category_id>", methods=["DELETE"])
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return jsonify({"message": "Category deleted"}), 200