from flask import request, jsonify, current_app as app
from functools import wraps
import jwt

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            try:
                token = request.headers['Authorization'].split()[1]
                print(f"[TOKEN] Received: {token}")
            except:
                print("[TOKEN] Authorization header found but could not parse token.")
                pass
        else:
            print("[TOKEN] No Authorization header found.")
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = data['user']
        except Exception as e:
            print(f"[TOKEN] Invalid token: {e}")
            return jsonify({'message': 'Token is invalid!'}), 401
        return f(current_user, *args, **kwargs)
    return decorated
