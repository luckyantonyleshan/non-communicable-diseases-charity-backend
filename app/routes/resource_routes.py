from flask import Blueprint, request, jsonify
from app.models.resource import Resource
from app.extensions import db

resource_bp = Blueprint("resources", __name__, url_prefix="/resources")

@resource_bp.route("/", methods=["GET"])
def get_resources():
    resources = Resource.query.all()
    return jsonify([{
        "id": resource.id,
        "title": resource.title,
        "url": resource.url
    } for resource in resources]), 200

@resource_bp.route("/", methods=["POST"])
def create_resource():
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