from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.user import User
from app.extensions import db

# Define the blueprint FIRST
user_bp = Blueprint('users', __name__, url_prefix='/users')

@user_bp.route('/me', methods=['GET'])
@jwt_required()
def get_current_user():
    try:
        user_id = get_jwt_identity()
        print(f"JWT Identity: {user_id}")  # Debug log
        user = User.query.get_or_404(user_id)
        return jsonify({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'role': user.role
        }), 200
    except Exception as e:
        print(f"Error in get_current_user: {str(e)}")  # Debug log
        return jsonify({'error': str(e)}), 500

@user_bp.route('/<int:id>/role', methods=['PATCH'])
@jwt_required()
def update_user_role(id):
    current_user = User.query.get_or_404(get_jwt_identity())
    if current_user.role != 'admin':
        return jsonify({'error': 'Admin access required'}), 403

    user = User.query.get_or_404(id)
    data = request.get_json()
    if not data or not data.get('role'):
        return jsonify({'error': 'Role is required'}), 400

    if data['role'] not in ['user', 'admin']:
        return jsonify({'error': 'Invalid role'}), 400

    user.role = data['role']
    db.session.commit()
    return jsonify({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'role': user.role
    }), 200