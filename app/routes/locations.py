from flask import Blueprint, request, jsonify
from ..utils.db_handler import read_db, write_db
from .token import token_required
import datetime

locations_bp = Blueprint('locations', __name__)

@locations_bp.route('/locations', methods=['GET'])
@token_required
def get_locations(current_user):
    db = read_db()
    locations = db['locations']
    loc_type = request.args.get('type')
    city = request.args.get('city')
    if loc_type:
        locations = [l for l in locations if l['type'] == loc_type]
    if city:
        locations = [l for l in locations if l['city'] == city]
    return jsonify(locations)

@locations_bp.route('/locations', methods=['POST'])
@token_required
def add_location(current_user):
    data = request.json
    db = read_db()
    new_loc = {
        'id': str(datetime.datetime.utcnow().timestamp()),
        'title': data['title'],
        'description': data['description'],
        'latitude': data['latitude'],
        'longitude': data['longitude'],
        'type': data['type'],
        'city': data['city']
    }
    db['locations'].append(new_loc)
    write_db(db)
    return jsonify(new_loc), 201

@locations_bp.route('/locations/<loc_id>', methods=['PUT'])
@token_required
def update_location(current_user, loc_id):
    data = request.json
    db = read_db()
    for loc in db['locations']:
        if loc['id'] == loc_id:
            loc.update({
                'title': data.get('title', loc['title']),
                'description': data.get('description', loc['description']),
                'latitude': data.get('latitude', loc['latitude']),
                'longitude': data.get('longitude', loc['longitude']),
                'type': data.get('type', loc['type']),
                'city': data.get('city', loc['city'])
            })
            write_db(db)
            return jsonify(loc)
    return jsonify({'message': 'Konum bulunamadı!'}), 404

@locations_bp.route('/locations/<loc_id>', methods=['DELETE'])
@token_required
def delete_location(current_user, loc_id):
    db = read_db()
    new_locations = [l for l in db['locations'] if l['id'] != loc_id]
    if len(new_locations) == len(db['locations']):
        return jsonify({'message': 'Konum bulunamadı!'}), 404
    db['locations'] = new_locations
    write_db(db)
    return jsonify({'message': 'Konum silindi.'})
