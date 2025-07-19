from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from app.models.user import User
from app.utilities.schemas import user_schema

user_bp = Blueprint("users", __name__)

@user_bp.route("/", methods=["GET"])
@jwt_required()
def get_users():
    users = User.query.all()
    return jsonify([user_schema(user) for user in users])
