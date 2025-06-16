from flask import Flask
from flask_cors import CORS
from .routes.auth import auth_bp
from .routes.locations import locations_bp
from .routes.root import root_bp
from .routes.users import users_bp

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'supersecretkey'

app.register_blueprint(auth_bp)
app.register_blueprint(locations_bp)
app.register_blueprint(root_bp)
app.register_blueprint(users_bp)
