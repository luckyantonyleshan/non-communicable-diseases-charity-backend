from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.extensions import db
from app.models.review import Review
from app.models.area import Area
from app.models.disease import Disease

review_bp = Blueprint('reviews', __name__, url_prefix='/reviews')

@review_bp.route('/', methods=['GET'])
def get_reviews():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    reviews = Review.query.paginate(page=page, per_page=per_page, error_out=False)
    return jsonify({
        'reviews': [review.to_dict() for review in reviews.items],
        'total': reviews.total,
        'pages': reviews.pages,
        'current_page': reviews.page
    }), 200

@review_bp.route('/', methods=['POST'])
@jwt_required()
def create_review():
    data = request.get_json()
    if not data or not all(key in data for key in ['content', 'area_id']):
        return jsonify({'error': 'Content and area_id are required'}), 400
    
    if len(data['content']) < 10 or len(data['content']) > 1000:
        return jsonify({'error': 'Content must be between 10 and 1000 characters'}), 400

    area = Area.query.get(data['area_id'])
    if not area:
        return jsonify({'error': 'Area not found'}), 404

    disease_id = data.get('disease_id')
    if disease_id:
        disease = Disease.query.get(disease_id)
        if not disease:
            return jsonify({'error': 'Disease not found'}), 404

    user_id = get_jwt_identity()
    review = Review(
        content=data['content'],
        user_id=user_id,
        area_id=data['area_id'],
        disease_id=disease_id if disease_id else None
    )
    db.session.add(review)
    db.session.commit()
    return jsonify(review.to_dict()), 201