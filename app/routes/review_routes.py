from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.review import Review
from app.models.area import Area
from app.models.disease import Disease  # Added import
from flask_jwt_extended import get_jwt_identity, jwt_required

review_bp = Blueprint("reviews", __name__, url_prefix="/reviews")

@review_bp.route("/", methods=["GET"])
def get_reviews():
    reviews = Review.query.all()
    return jsonify([review.to_dict() for review in reviews]), 200

@review_bp.route("/", methods=["POST"])
@jwt_required()
def create_review():
    data = request.get_json()
    
    # Validate required fields
    if not data or not all(key in data for key in ["content", "area_id"]):
        return jsonify({"error": "Content and area_id are required"}), 400
    
    # Validate area exists
    area = Area.query.get(data["area_id"])
    if not area:
        return jsonify({"error": "Area not found"}), 404
    
    # Validate disease exists if provided
    if "disease_id" in data and data["disease_id"]:
        disease = Disease.query.get(data["disease_id"])
        if not disease:
            return jsonify({"error": "Disease not found"}), 404

    review = Review(
        content=data["content"],
        user_id=get_jwt_identity(),
        disease_id=data.get("disease_id"),
        area_id=data["area_id"]
    )
    
    try:
        db.session.add(review)
        db.session.commit()
        return jsonify(review.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500