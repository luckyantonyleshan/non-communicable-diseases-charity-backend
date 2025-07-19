from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

user_bp = Blueprint("users", __name__)

@user_bp.route("/")
@jwt_required()
def profile():
    return jsonify(message="User profile access successful")
