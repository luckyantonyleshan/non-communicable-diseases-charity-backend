from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.user import User
from app.utilities.jwt_helpers import generate_token

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    user = User(username=data["username"], email=data["email"])
    user.set_password(data["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify(message="User registered successfully"), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(username=data["username"]).first()
    if user and user.check_password(data["password"]):
        token = generate_token(user)
        return jsonify(token=token), 200
    return jsonify(message="Invalid credentials"), 401
