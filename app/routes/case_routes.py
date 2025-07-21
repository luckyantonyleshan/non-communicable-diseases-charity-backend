from flask import Blueprint, request, jsonify
from app.models.case import Case
from app.extensions import db

case_bp = Blueprint("cases", __name__, url_prefix="/cases")

@case_bp.route("/", methods=["GET"])
def get_cases():
    cases = Case.query.all()
    return jsonify([{
        "id": case.id,
        "title": case.title,
        "description": case.description,
        "user_id": case.user_id
    } for case in cases]), 200

@case_bp.route("/", methods=["POST"])
def create_case():
    data = request.get_json()
    if not data or not data.get("title") or not data.get("description"):
        return jsonify({"error": "Title and description are required"}), 400

    case = Case(title=data["title"], description=data["description"], user_id=data.get("user_id"))
    db.session.add(case)
    db.session.commit()
    return jsonify({
        "id": case.id,
        "title": case.title,
        "description": case.description,
        "user_id": case.user_id
    }), 201