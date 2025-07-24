from flask import Blueprint, request
from controllers.auth_controller import signup, login

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods = ['POST'])
def handle_signup():
    return signup(request.get_json(force=True))

@auth_bp.route('/login', methods = ['POST'])
def handle_login():
    return login(request.get_json(force=True))