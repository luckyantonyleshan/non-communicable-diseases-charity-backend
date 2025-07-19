from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.case import Case

case_bp = Blueprint("cases", __name__)

@case_bp.route("/", methods=["GET"])
def get_cases():
    cases = Case.query.all()
    return jsonify([{"id": c.id, "title": c.title, "description": c.description} for c in cases])

@case_bp.route("/", methods=["POST"])
def create_case():
    data = request.json
    case = Case(title=data["title"], description=data["description"])
    db.session.add(case)
    db.session.commit()
    return jsonify(message="Case created"), 201
