from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import app.models.donation
import app.extensions
import app.schemas

donation_bp = Blueprint("donations", __name__)

@donation_bp.route("/", methods=["GET"])
def get_donations():
    donations = app.models.donation.Donation.query.all()
    return jsonify([app.schemas.donation_schema(d) for d in donations])

@donation_bp.route("/", methods=["POST"])
@jwt_required()
def create_donation():
    data = request.get_json()
    donation = app.models.donation.Donation(amount=data["amount"], donor_name=data["donor_name"], user_id=data["user_id"])
    app.extensions.db.session.add(donation)
    app.extensions.db.session.commit()
    return jsonify(app.schemas.donation_schema(donation)), 201