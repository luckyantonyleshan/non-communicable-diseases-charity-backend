from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.models.resource import Resource
from app.utilities.extensions import db
from app.utilities.schemas import resource_schema

resource_bp = Blueprint("resources", __name__)

@resource_bp.route("/", methods=["GET"])
def get_resources():
    resources = Resource.query.all()
    return jsonify([resource_schema(r) for r in resources])

@resource_bp.route("/", methods=["POST"])
@jwt_required()
def create_resource():
    data = request.get_json()
    resource = Resource(
        name=data["name"],
        description=data["description"],
        quantity=data["quantity"],
        case_id=data["case_id"]
    )
    db.session.add(resource)
    db.session.commit()
    return jsonify(resource_schema(resource)), 201
