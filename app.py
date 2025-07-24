from flask import Flask
from flask_cors import CORS
from routes import auth, meals, menus, orders  # Import your route blueprints
from config import Config  # Your custom config file

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)

    # Register Blueprints
    app.register_blueprint(auth.auth_bp, url_prefix='/auth')
   

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
