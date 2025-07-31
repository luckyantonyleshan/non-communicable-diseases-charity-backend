from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.user import User
from app.extensions import db
import logging

user_bp = Blueprint('users', __name__, url_prefix='/users')
logger = logging.getLogger(__name__)

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
            'role': user.role
        }), 200
    except Exception as e:
        logger.error(f"Get current user error: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

@user_bp.route('/<int:user_id>/role', methods=['PATCH'])
@jwt_required()
def update_user_role(user_id):
    try:
        current_user = User.query.get(get_jwt_identity())
        if current_user.role != 'admin':
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
        logger.error(f"Update role error: {str(e)}")
        db.session.rollback()
        return jsonify({'error': 'Role update failed'}), 500