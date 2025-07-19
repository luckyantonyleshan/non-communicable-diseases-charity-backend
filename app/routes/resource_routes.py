from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.resource import Resource

resource_bp = Blueprint("resources", __name__)

@resource_bp.route("/", methods=["GET"])
def get_resources():
    resources = Resource.query.all()
    return jsonify([{"id": r.id, "title": r.title, "url": r.url} for r in resources])

@resource_bp.route("/", methods=["POST"])
def add_resource():
    data = request.json
    resource = Resource(title=data["title"], url=data["url"])
    db.session.add(resource)
    db.session.commit()
    return jsonify(message="Resource added"), 201
