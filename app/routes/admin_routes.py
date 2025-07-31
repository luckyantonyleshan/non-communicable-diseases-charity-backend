from functools import wraps
from datetime import datetime
from flask import Blueprint, jsonify, request, g
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.user import User
from app.models.case import Case
from app.models.donation import Donation
from app.extensions import db

# Initialize admin Blueprint
admin_bp = Blueprint('admin_bp', __name__, url_prefix='/api/admin')

# Custom admin required decorator
def admin_required(fn):
    @jwt_required()
    @wraps(fn)
    def wrapper(*args, **kwargs):
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)
        
        if not user or user.role != 'admin':
            return jsonify({
                'success': False,
                'error': 'Admin privileges required'
            }), 403
            
        g.current_user = user
        return fn(*args, **kwargs)
    return wrapper

@admin_bp.route('/users', methods=['GET'])
@admin_required
def get_all_users():
    """Get all users (admin only)"""
    try:
        users = User.query.order_by(User.created_at.desc()).all()
        
        return jsonify({
            'success': True,
            'count': len(users),
            'users': [{
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'role': user.role,
                'created_at': user.created_at.isoformat() if user.created_at else None,
                'case_count': len(user.cases),
                'donation_count': len(user.donations)
            } for user in users]
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@admin_bp.route('/users/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
@admin_required
def manage_user(user_id):
    """Manage individual users (admin only)"""
    user = User.query.get_or_404(user_id)
    
    if request.method == 'GET':
        return jsonify({
            'success': True,
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'role': user.role,
                'created_at': user.created_at.isoformat(),
                'cases': [case.id for case in user.cases],
                'donations': [donation.id for donation in user.donations]
            }
        }), 200
        
    elif request.method == 'PUT':
        data = request.get_json()
        
        # Validate input
        if not data:
            return jsonify({
                'success': False,
                'error': 'No data provided'
            }), 400
            
        # Update user fields
        if 'role' in data and data['role'] in ['user', 'admin']:
            user.role = data['role']
            
        if 'username' in data and data['username']:
            if User.query.filter(User.username == data['username'], User.id != user.id).first():
                return jsonify({
                    'success': False,
                    'error': 'Username already taken'
                }), 400
            user.username = data['username']
            
        if 'email' in data and data['email']:
            if User.query.filter(User.email == data['email'], User.id != user.id).first():
                return jsonify({
                    'success': False,
                    'error': 'Email already registered'
                }), 400
            user.email = data['email']
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'User updated successfully',
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'role': user.role
            }
        }), 200
        
    elif request.method == 'DELETE':
        db.session.delete(user)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'User deleted successfully'
        }), 200

@admin_bp.route('/cases', methods=['GET'])
@admin_required
def get_all_cases():
    """Get all cases (admin only)"""
    try:
        cases = Case.query.order_by(Case.created_at.desc()).all()
        
        return jsonify({
            'success': True,
            'count': len(cases),
            'cases': [{
                'id': case.id,
                'title': case.title,
                'description': case.description,
                'target_amount': float(case.target_amount),
                'current_amount': float(case.current_amount),
                'status': case.status,
                'user_id': case.user_id,
                'created_at': case.created_at.isoformat(),
                'donation_count': len(case.donations)
            } for case in cases]
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@admin_bp.route('/donations', methods=['GET'])
@admin_required
def get_all_donations():
    """Get all donations (admin only)"""
    try:
        donations = Donation.query.order_by(Donation.created_at.desc()).all()
        
        return jsonify({
            'success': True,
            'count': len(donations),
            'donations': [{
                'id': donation.id,
                'amount': float(donation.amount),
                'message': donation.message,
                'is_anonymous': donation.is_anonymous,
                'user_id': donation.user_id,
                'case_id': donation.case_id,
                'created_at': donation.created_at.isoformat()
            } for donation in donations]
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@admin_bp.route('/stats', methods=['GET'])
@admin_required
def get_admin_stats():
    """Get admin dashboard statistics"""
    try:
        stats = {
            'total_users': User.query.count(),
            'total_cases': Case.query.count(),
            'total_donations': Donation.query.count(),
            'total_donation_amount': float(db.session.query(
                db.func.sum(Donation.amount)
            ).scalar() or 0),
            'active_cases': Case.query.filter_by(status='active').count(),
            'completed_cases': Case.query.filter_by(status='completed').count()
        }
        
        return jsonify({
            'success': True,
            'stats': stats
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
