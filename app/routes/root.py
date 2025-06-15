from flask import Blueprint, jsonify

root_bp = Blueprint('root', __name__)

@root_bp.route('/', methods=['GET'])
def root():
    return jsonify({
        'message': 'API kullanılabilir. Endpointleri görmek için README dosyasına bakınız.'
    })
