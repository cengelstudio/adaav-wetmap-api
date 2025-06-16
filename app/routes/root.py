from flask import Blueprint, jsonify

root_bp = Blueprint('root', __name__, url_prefix='/api')

@root_bp.route('/', methods=['GET'])
def root():
    return jsonify({
        'message': 'API is available. See README for endpoints.'
    })
