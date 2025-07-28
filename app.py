from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from . import db
from .config import Config


from .controllers.auth_controller import auth_bp
from .controllers.meal_controller import meal_bp
from .controllers.menu_controller import menu_bp
from .controllers.order_controller import order_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

 
    db.init_app(app)
    Migrate(app, db)
    CORS(app)


    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(meal_bp, url_prefix='/meals')
    app.register_blueprint(menu_bp, url_prefix='/menus')
    app.register_blueprint(order_bp, url_prefix='/orders')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
