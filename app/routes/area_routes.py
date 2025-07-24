from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.extensions import db
from app.models.area import Area
from app.models.user import User

area_bp = Blueprint('areas', __name__, url_prefix='/areas')

@area_bp.route('/', methods=['GET'])
def get_areas():
    areas = Area.query.all()
    return jsonify([{
        'id': area.id,
        'name': area.name,
        'description': area.description,
        'latitude': area.latitude,
        'longitude': area.longitude,
        'created_at': area.created_at.isoformat()
    } for area in areas]), 200

@area_bp.route('/<int:id>', methods=['GET'])
def get_area(id):
    area = Area.query.get_or_404(id)
    return jsonify({
        'id': area.id,
        'name': area.name,
        'description': area.description,
        'latitude': area.latitude,
        'longitude': area.longitude,
        'created_at': area.created_at.isoformat()
    }), 200

@area_bp.route('/map', methods=['GET'])
def get_map_data():
    areas = Area.query.all()
    geojson = {
        'type': 'FeatureCollection',
        'features': [{
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [area.longitude, area.latitude]
            },
            'properties': {
                'id': area.id,
                'name': area.name,
                'description': area.description
            }
        } for area in areas if area.latitude and area.longitude]
    }
    return jsonify(geojson), 200

@area_bp.route('/', methods=['POST'])
@jwt_required()
def create_area():
    user = User.query.get_or_404(get_jwt_identity())
    if user.role != 'admin':
        return jsonify({'error': 'Admin access required'}), 403

    data = request.get_json()
    required_fields = ['name', 'description']
    if not data or any(field not in data for field in required_fields):
        return jsonify({'error': 'Name and description are required'}), 400

    latitude = data.get('latitude')
    longitude = data.get('longitude')
    if latitude and longitude:
        try:
            latitude = float(latitude)
            longitude = float(longitude)
            if not (-90 <= latitude <= 90) or not (-180 <= longitude <= 180):
                raise ValueError
        except (ValueError, TypeError):
            return jsonify({'error': 'Invalid latitude or longitude'}), 400

    area = Area(name=data['name'], description=data['description'], latitude=latitude, longitude=longitude)
    db.session.add(area)
    db.session.commit()
    return jsonify({
        'id': area.id,
        'name': area.name,
        'description': area.description,
        'latitude': area.latitude,
        'longitude': area.longitude,
        'created_at': area.created_at.isoformat()
    }), 201

@area_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_area(id):
    user = User.query.get_or_404(get_jwt_identity())
    if user.role != 'admin':
        return jsonify({'error': 'Admin access required'}), 403

    area = Area.query.get_or_404(id)
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    if 'name' in data:
        area.name = data['name']
    if 'description' in data:
        area.description = data['description']
    if 'latitude' in data and 'longitude' in data:
        try:
            latitude = float(data['latitude'])
            longitude = float(data['longitude'])
            if not (-90 <= latitude <= 90) or not (-180 <= longitude <= 180):
                raise ValueError
            area.latitude = latitude
            area.longitude = longitude
        except (ValueError, TypeError):
            return jsonify({'error': 'Invalid latitude or longitude'}), 400

    db.session.commit()
    return jsonify({
        'id': area.id,
        'name': area.name,
        'description': area.description,
        'latitude': area.latitude,
        'longitude': area.longitude,
        'created_at': area.created_at.isoformat()
    }), 200

@area_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_area(id):
    user = User.query.get_or_404(get_jwt_identity())
    if user.role != 'admin':
        return jsonify({'error': 'Admin access required'}), 403

    area = Area.query.get_or_404(id)
    db.session.delete(area)
    db.session.commit()
    return jsonify({'message': 'Area deleted'}), 200