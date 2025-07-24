# routes/disease_routes.py
from flask import Blueprint, request, jsonify
from app.extensions import db, jwt
from app.models.disease import Disease
from app.models.user import User  # Added missing import
from flask_jwt_extended import get_jwt_identity, jwt_required

disease_bp = Blueprint("diseases", __name__, url_prefix="/diseases")

@disease_bp.route("/", methods=["GET"])
def get_diseases():
    diseases = Disease.query.all()
    return jsonify([disease.to_dict() for disease in diseases]), 200

@disease_bp.route("/", methods=["POST"])
@jwt_required()
def create_disease():
    data = request.get_json()
    if not all(key in data for key in ["name", "description", "prevalence"]):
        return jsonify({"error": "Name, description, and prevalence are required"}), 400

    current_user = User.query.get(get_jwt_identity())
    if current_user.role != "admin":
        return jsonify({"error": "Admin access required"}), 403

    try:
        prevalence = float(data["prevalence"])
        if prevalence < 0 or prevalence > 100:
            raise ValueError
    except (ValueError, TypeError):
        return jsonify({"error": "Prevalence must be a number between 0 and 100"}), 400

    disease = Disease(
        name=data["name"],
        description=data["description"],
        prevalence=prevalence
    )
    db.session.add(disease)
    db.session.commit()
    return jsonify(disease.to_dict()), 201