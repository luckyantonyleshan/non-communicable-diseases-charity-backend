from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
import app.models.user
import app.schemas

user_bp = Blueprint("users", __name__)

@user_bp.route("/", methods=["GET"])
@jwt_required()
def get_users():
    users = app.models.user.User.query.all()
    return jsonify([app.schemas.user_schema(user) for user in users])