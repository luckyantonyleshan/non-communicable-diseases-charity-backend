from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import app.models.case
import app.extensions
import app.schemas

case_bp = Blueprint("cases", __name__)

@case_bp.route("/", methods=["GET"])
def get_cases():
    cases = app.models.case.Case.query.all()
    return jsonify([app.schemas.case_schema(case) for case in cases])

@case_bp.route("/", methods=["POST"])
@jwt_required()
def create_case():
    data = request.get_json()
    case = app.models.case.Case(title=data["title"], description=data["description"], user_id=data["user_id"])
    app.extensions.db.session.add(case)
    app.extensions.db.session.commit()
    return jsonify(app.schemas.case_schema(case)), 201