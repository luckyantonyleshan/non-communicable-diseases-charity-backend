from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.case import Case
from app.models.user import User
from app.extensions import db

case_bp = Blueprint("cases", __name__, url_prefix="/cases")

@case_bp.route("/", methods=["GET"])
def get_cases():
    try:
        cases = Case.query.all()
        return jsonify([{
            "id": case.id,
            "title": case.title,
            "description": case.description,
            "amount_needed": float(case.amount_needed),
            "amount_received": float(case.amount_received),
            "user_id": case.user_id,
            "username": case.user.username if case.user else None
        } for case in cases]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@case_bp.route("/", methods=["POST"])
@jwt_required()
def create_case():
    try:
        data = request.get_json()
        
        required_fields = ["title", "description", "amount_needed"]
        if not data or any(field not in data for field in required_fields):
            return jsonify({
                "error": "Title, description, and amount_needed are required fields"
            }), 400
        
        try:
            amount_needed = float(data["amount_needed"])
            if amount_needed <= 0:
                raise ValueError
        except (ValueError, TypeError):
            return jsonify({
                "error": "amount_needed must be a positive number"
            }), 400

        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404

        case = Case(
            title=data["title"],
            description=data["description"],
            amount_needed=amount_needed,
            amount_received=0.0,
            user_id=user_id
        )
        
        db.session.add(case)
        db.session.commit()
        
        return jsonify({
            "id": case.id,
            "title": case.title,
            "description": case.description,
            "amount_needed": float(case.amount_needed),
            "amount_received": float(case.amount_received),
            "user_id": case.user_id
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@case_bp.route("/<int:case_id>", methods=["GET"])
def get_case(case_id):
    try:
        case = Case.query.get_or_404(case_id)
        return jsonify({
            "id": case.id,
            "title": case.title,
            "description": case.description,
            "amount_needed": float(case.amount_needed),
            "amount_received": float(case.amount_received),
            "user_id": case.user_id,
            "username": case.user.username if case.user else None
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
