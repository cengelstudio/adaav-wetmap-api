from flask import Blueprint, request, jsonify, current_app as app
import jwt
import datetime
from ..utils.db_handler import read_db
from .token import token_required

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    db = read_db()
    user = next((u for u in db['users'] if u['username'] == data.get('username') and u['password'] == data.get('password')), None)
    if not user:
        return jsonify({'message': 'Kullanıcı adı veya şifre hatalı!'}), 401
    token = jwt.encode({'user': {'id': user['id'], 'name': user['name'], 'username': user['username']}, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=12)}, app.config['SECRET_KEY'], algorithm="HS256")
    return jsonify({'token': token, 'user': {'id': user['id'], 'name': user['name'], 'username': user['username']}})

@auth_bp.route('/me', methods=['GET'])
@token_required
def me(current_user):
    return jsonify(current_user)
