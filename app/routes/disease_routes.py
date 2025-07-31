from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.extensions import db
from app.models.disease import Disease
from app.models.user import User

disease_bp = Blueprint("diseases", __name__, url_prefix="/diseases")

@disease_bp.route("/", methods=["GET"])
def get_diseases():
    try:
        diseases = Disease.query.all()
        return jsonify([disease.to_dict() for disease in diseases]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@disease_bp.route("/", methods=["POST"])
@jwt_required()
def create_disease():
    try:
        data = request.get_json()
        if not all(key in data for key in ["name", "description", "prevalence"]):
            return jsonify({"error": "Name, description, and prevalence are required"}), 400

        # Check if user is admin
        user_id = get_jwt_identity()
        current_user = User.query.get(user_id)
        if not current_user or current_user.role != "admin":
            return jsonify({"error": "Admin access required"}), 403

        # Validate prevalence
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
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
