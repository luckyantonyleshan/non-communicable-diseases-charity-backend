from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from app.models.user import User
import logging

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
logger = logging.getLogger(__name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()
        if not data or not data.get("username") or not data.get("password"):
            return jsonify({"error": "Username and password required"}), 400

        user = User.query.filter_by(username=data["username"]).first()
        if not user or not user.check_password(data["password"]):
            return jsonify({"error": "Invalid credentials"}), 401

        # Create token with user identity as dictionary
        access_token = create_access_token(identity={
            "id": user.id,
            "username": user.username,
            "role": user.role
        })
        
        return jsonify({
            "access_token": access_token,
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "role": user.role
            }
        }), 200
    except Exception as e:
        logger.error(f"Login error: {str(e)}")
        return jsonify({"error": "Login failed"}), 500