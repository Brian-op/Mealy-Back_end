from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy

def create_app():
    app = Flask(__name__)
    app.config['SQLACHEMY_DATABASE_URI'] = 'sqlalchemy:///mealy.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)


    return app