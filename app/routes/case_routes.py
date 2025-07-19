from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.models.case import Case
from app.utilities.extensions import db
from app.utilities.schemas import case_schema

case_bp = Blueprint("cases", __name__)

@case_bp.route("/", methods=["GET"])
def get_cases():
    cases = Case.query.all()
    return jsonify([case_schema(case) for case in cases])

@case_bp.route("/", methods=["POST"])
@jwt_required()
def create_case():
    data = request.get_json()
    case = Case(title=data["title"], description=data["description"], user_id=data["user_id"])
    db.session.add(case)
    db.session.commit()
    return jsonify(case_schema(case)), 201
