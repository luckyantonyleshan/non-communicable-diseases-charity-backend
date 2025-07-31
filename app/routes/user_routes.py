from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.user import User
from app.extensions import db

user_bp = Blueprint('users', __name__, url_prefix='/users')

@user_bp.route('/me', methods=['GET'])
@jwt_required()
def get_current_user():
    try:
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        return jsonify({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'role': user.role,
            'created_at': user.created_at.isoformat() if user.created_at else None
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@user_bp.route('/', methods=['GET'])
@jwt_required()
def get_all_users():
    try:
        current_user_id = get_jwt_identity()
        current_user = User.query.get(current_user_id)
        
        if not current_user or current_user.role != 'admin':
            return jsonify({'error': 'Admin access required'}), 403

        users = User.query.all()
        return jsonify({
            'users': [{
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'role': user.role,
                'created_at': user.created_at.isoformat() if user.created_at else None
            } for user in users]
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@user_bp.route('/<int:user_id>/role', methods=['PATCH'])
@jwt_required()
def update_user_role(user_id):
    try:
        current_user_id = get_jwt_identity()
        current_user = User.query.get(current_user_id)
        
        if not current_user or current_user.role != 'admin':
            return jsonify({'error': 'Admin access required'}), 403

        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        data = request.get_json()
        if not data or 'role' not in data:
            return jsonify({'error': 'Role is required'}), 400

        if data['role'] not in ['user', 'admin']:
            return jsonify({'error': 'Invalid role'}), 400

        user.role = data['role']
        db.session.commit()

        return jsonify({
            'message': 'Role updated successfully',
            'user': {
                'id': user.id,
                'username': user.username,
                'role': user.role
            }
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
