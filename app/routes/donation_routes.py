from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.extensions import db
from app.models.donation import Donation
from app.models.user import User
from app.models.case import Case

donation_bp = Blueprint("donations", __name__, url_prefix="/donations")

@donation_bp.route("/", methods=["GET"])
def get_donations():
    try:
        donations = Donation.query.all()
        return jsonify([donation.to_dict() for donation in donations]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@donation_bp.route("/", methods=["POST"])
@jwt_required()
def create_donation():
    try:
        data = request.get_json()
        if not all(key in data for key in ["amount", "donor_name"]):
            return jsonify({"error": "Amount and donor_name are required"}), 400

        try:
            amount = float(data["amount"])
            if amount <= 0:
                raise ValueError
        except (ValueError, TypeError):
            return jsonify({"error": "Amount must be a positive number"}), 400

        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404

        case_id = data.get("case_id")
        if case_id:
            case = Case.query.get(case_id)
            if not case:
                return jsonify({"error": "Case not found"}), 404
            
            case.amount_received += amount
            
        donation = Donation(
            amount=amount,
            donor_name=data["donor_name"],
            user_id=user_id,
            case_id=case_id,
            area_id=data.get("area_id")
        )
        
        db.session.add(donation)
        db.session.commit()
        
        return jsonify(donation.to_dict()), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
