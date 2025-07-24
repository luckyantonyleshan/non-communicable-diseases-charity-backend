# routes/donation_routes.py
from flask import Blueprint, request, jsonify
from app.extensions import db, jwt
from app.models.donation import Donation
from app.models.user import User
from app.models.case import Case  # Added for validation
from flask_jwt_extended import get_jwt_identity, jwt_required

donation_bp = Blueprint("donations", __name__, url_prefix="/donations")

@donation_bp.route("/", methods=["GET"])
def get_donations():
    donations = Donation.query.all()
    return jsonify([donation.to_dict() for donation in donations]), 200

@donation_bp.route("/", methods=["POST"])
@jwt_required()
def create_donation():
    data = request.get_json()
    if not all(key in data for key in ["amount", "donor_name", "case_id"]):
        return jsonify({"error": "Amount, donor_name, and case_id are required"}), 400

    # Validate case exists
    case = Case.query.get(data["case_id"])
    if not case:
        return jsonify({"error": "Case not found"}), 404

    try:
        amount = float(data["amount"])
        if amount <= 0:
            raise ValueError
    except (ValueError, TypeError):
        return jsonify({"error": "Amount must be a positive number"}), 400

    user = User.query.get_or_404(get_jwt_identity())
    donation = Donation(
        amount=amount,
        donor_name=data["donor_name"],
        user_id=user.id,
        case_id=data["case_id"]
    )
    db.session.add(donation)
    db.session.commit()
    return jsonify(donation.to_dict()), 201