from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.donation import Donation

donation_bp = Blueprint("donations", __name__)

@donation_bp.route("/", methods=["GET"])
def get_donations():
    donations = Donation.query.all()
    return jsonify([{"id": d.id, "amount": d.amount, "donor_name": d.donor_name} for d in donations])

@donation_bp.route("/", methods=["POST"])
def create_donation():
    data = request.json
    donation = Donation(amount=data["amount"], donor_name=data["donor_name"])
    db.session.add(donation)
    db.session.commit()
    return jsonify(message="Donation added"), 201
