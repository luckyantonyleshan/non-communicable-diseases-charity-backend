from flask import Blueprint, request, jsonify
from app.models.donation import Donation
from app.extensions import db

donation_bp = Blueprint("donations", __name__, url_prefix="/donations")

@donation_bp.route("/", methods=["GET"])
def get_donations():
    donations = Donation.query.all()
    return jsonify([{
        "id": donation.id,
        "amount": donation.amount,
        "donor_name": donation.donor_name,
        "user_id": donation.user_id
    } for donation in donations]), 200

@donation_bp.route("/", methods=["POST"])
def create_donation():
    data = request.get_json()
    if not data or not data.get("amount") or not data.get("donor_name"):
        return jsonify({"error": "Amount and donor name are required"}), 400

    donation = Donation(amount=data["amount"], donor_name=data["donor_name"], user_id=data.get("user_id"))
    db.session.add(donation)
    db.session.commit()
    return jsonify({
        "id": donation.id,
        "amount": donation.amount,
        "donor_name": donation.donor_name,
        "user_id": donation.user_id
    }), 201