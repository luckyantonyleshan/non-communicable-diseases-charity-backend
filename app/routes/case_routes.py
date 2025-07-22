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
        "amount_needed": case.amount_needed,
        "amount_received": case.amount_received,
        "user_id": case.user_id
    } for case in cases]), 200

@case_bp.route("/", methods=["POST"])
def create_case():
    data = request.get_json()
    
    # Validate required fields
    required_fields = ["title", "description", "amount_needed"]
    if not data or any(field not in data for field in required_fields):
        return jsonify({
            "error": "Title, description, and amount_needed are required fields"
        }), 400
    
    # Validate amount_needed is a positive number
    try:
        amount_needed = float(data["amount_needed"])
        if amount_needed <= 0:
            raise ValueError
    except (ValueError, TypeError):
        return jsonify({
            "error": "amount_needed must be a positive number"
        }), 400

    # Create case with all required fields
    case = Case(
        title=data["title"],
        description=data["description"],
        amount_needed=amount_needed,
        amount_received=0.0,  # Default value
        user_id=data.get("user_id")  # Optional field
    )
    
    db.session.add(case)
    db.session.commit()
    
    return jsonify({
        "id": case.id,
        "title": case.title,
        "description": case.description,
        "amount_needed": case.amount_needed,
        "amount_received": case.amount_received,
        "user_id": case.user_id
    }), 201