from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import app.models.resource
import app.extensions
import app.schemas

resource_bp = Blueprint("resources", __name__)

@resource_bp.route("/", methods=["GET"])
def get_resources():
    resources = app.models.resource.Resource.query.all()
    return jsonify([app.schemas.resource_schema(r) for r in resources])

@resource_bp.route("/", methods=["POST"])
@jwt_required()
def create_resource():
    data = request.get_json()
    resource = app.models.resource.Resource(title=data["title"], url=data["url"])
    app.extensions.db.session.add(resource)
    app.extensions.db.session.commit()
    return jsonify(app.schemas.resource_schema(resource)), 201