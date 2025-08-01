from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.models.user import User
from app.extensions import db

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        
        required = ['username', 'email', 'password']
        if not all(field in data for field in required):
            return jsonify({"error": "Missing required fields"}), 400
        
        if User.query.filter((User.username == data['username']) | 
                            (User.email == data['email'])).first():
            return jsonify({"error": "Username or email already exists"}), 400
        
        user = User(
            username=data['username'],
            email=data['email'],
            role=data.get('role', 'user')
        )
        user.set_password(data['password'])
        db.session.add(user)
        db.session.commit()
        
        access_token = create_access_token(identity=user.id)
        
        return jsonify({
            'message': 'User registered successfully',
            'access_token': access_token,
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'role': user.role
            }
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        
        if not data or 'username' not in data or 'password' not in data:
            return jsonify({"error": "Username and password required"}), 400
        
        user = User.query.filter_by(username=data['username']).first()
        if not user or not user.check_password(data['password']):
            return jsonify({"error": "Invalid credentials"}), 401
        
        access_token = create_access_token(identity=user.id)
        
        return jsonify({
            'message': 'Login successful',
            'access_token': access_token,
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'role': user.role
            }
        }), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500
