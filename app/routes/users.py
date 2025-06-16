from flask import Blueprint, request, jsonify
from ..utils.db_handler import read_users, write_users
from .token import token_required
import datetime

users_bp = Blueprint('users', __name__, url_prefix='/api/users')

# Yardımcı fonksiyon: isAdmin belirle
ADMIN_IDS = {'1', '2', '3'}
def user_to_dict(user):
    return {
        'id': user['id'],
        'name': user['name'],
        'username': user['username'],
        'role': user.get('role', 'AUTHORIZED_PERSON'),
        'isAdmin': user['id'] in ADMIN_IDS
    }

@users_bp.route('/', methods=['GET'])
@token_required
def list_users(current_user):
    users = read_users()
    return jsonify({'users': [user_to_dict(u) for u in users]})

@users_bp.route('/', methods=['POST'])
@token_required
def add_user(current_user):
    data = request.json
    users = read_users()
    new_id = str(int(datetime.datetime.utcnow().timestamp() * 1000))
    user = {
        'id': new_id,
        'name': data['name'],
        'username': data['username'],
        'password': data['password'],
        'role': data.get('role', 'AUTHORIZED_PERSON')
    }
    users.append(user)
    write_users(users)
    return jsonify({'user': user_to_dict(user)})

@users_bp.route('/<user_id>', methods=['PUT'])
@token_required
def update_user(current_user, user_id):
    data = request.json
    users = read_users()
    for user in users:
        if user['id'] == user_id:
            user['name'] = data.get('name', user['name'])
            user['username'] = data.get('username', user['username'])
            if 'password' in data:
                user['password'] = data['password']
            if 'role' in data:
                user['role'] = data['role']
            write_users(users)
            return jsonify({'user': user_to_dict(user)})
    return jsonify({'message': 'Kullanıcı bulunamadı!'}), 404

@users_bp.route('/<user_id>', methods=['DELETE'])
@token_required
def delete_user(current_user, user_id):
    if current_user['id'] == user_id:
        return jsonify({'success': False, 'message': 'Kendi hesabınızı silemezsiniz!'}), 403
    users = read_users()
    new_users = [u for u in users if u['id'] != user_id]
    if len(new_users) == len(users):
        return jsonify({'success': False, 'message': 'Kullanıcı bulunamadı!'}), 404
    write_users(new_users)
    return jsonify({'success': True, 'message': 'Kullanıcı silindi.'})

@users_bp.route('/<user_id>', methods=['GET'])
@token_required
def get_user(current_user, user_id):
    users = read_users()
    for user in users:
        if user['id'] == user_id:
            return jsonify({'user': user_to_dict(user)})
    return jsonify({'message': 'Kullanıcı bulunamadı!'}), 404
