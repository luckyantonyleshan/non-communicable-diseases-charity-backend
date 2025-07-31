from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.resource import Resource
from app.models.user import User
from app.extensions import db

resource_bp = Blueprint("resources", __name__, url_prefix="/resources")

@resource_bp.route("/", methods=["GET"])
def get_resources():
    try:
        resources = Resource.query.all()
        return jsonify([{
            "id": resource.id,
            "title": resource.title,
            "url": resource.url
        } for resource in resources]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@resource_bp.route("/", methods=["POST"])
@jwt_required()
def create_resource():
    try:
        # Check if user is admin
        user_id = get_jwt_identity()
        current_user = User.query.get(user_id)
        if not current_user or current_user.role != "admin":
            return jsonify({"error": "Admin access required"}), 403
            
        data = request.get_json()
        if not data or not data.get("title") or not data.get("url"):
            return jsonify({"error": "Title and URL are required"}), 400

        resource = Resource(title=data["title"], url=data["url"])
        db.session.add(resource)
        db.session.commit()
        return jsonify({
            "id": resource.id,
            "title": resource.title,
            "url": resource.url
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
