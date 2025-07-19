from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.models.donation import Donation
from app.utilities.extensions import db
from app.utilities.schemas import donation_schema

donation_bp = Blueprint("donations", __name__)

@donation_bp.route("/", methods=["GET"])
def get_donations():
    donations = Donation.query.all()
    return jsonify([donation_schema(d) for d in donations])

@donation_bp.route("/", methods=["POST"])
@jwt_required()
def create_donation():
    data = request.get_json()
    donation = Donation(amount=data["amount"], user_id=data["user_id"])
    db.session.add(donation)
    db.session.commit()
    return jsonify(donation_schema(donation)), 201
