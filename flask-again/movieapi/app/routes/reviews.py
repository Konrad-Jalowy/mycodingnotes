from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import Review

reviews_bp = Blueprint('reviews_bp', __name__)

@reviews_bp.route("/", methods=["GET"])
def get_reviews():
    reviews = Review.query.all()
    results = []
    for review in reviews:
        results.append({
            "id": review.id,
            "text": review.text,
            "rating": review.rating,
            "movie_id": review.movie_id
        })
    return jsonify(results), 200

@reviews_bp.route("/", methods=["POST"])
def create_review():
    data = request.get_json()
    text = data.get("text")
    rating = data.get("rating")
    movie_id = data.get("movie_id")

    review = Review(text=text, rating=rating, movie_id=movie_id)
    db.session.add(review)
    db.session.commit()
    return jsonify({"message": "Review created", "review_id": review.id}), 201

@reviews_bp.route("/<int:review_id>", methods=["GET"])
def get_review(review_id):
    review = Review.query.get_or_404(review_id)
    return jsonify({
        "id": review.id,
        "text": review.text,
        "rating": review.rating,
        "movie_id": review.movie_id
    }), 200

@reviews_bp.route("/<int:review_id>", methods=["PUT", "PATCH"])
def update_review(review_id):
    review = Review.query.get_or_404(review_id)
    data = request.get_json()
    review.text = data.get("text", review.text)
    review.rating = data.get("rating", review.rating)
    db.session.commit()
    return jsonify({"message": "Review updated"}), 200

@reviews_bp.route("/<int:review_id>", methods=["DELETE"])
def delete_review(review_id):
    review = Review.query.get_or_404(review_id)
    db.session.delete(review)
    db.session.commit()
    return jsonify({"message": "Review deleted"}), 200
