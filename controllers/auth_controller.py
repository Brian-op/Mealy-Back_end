from flask import Blueprint, request
from ..models.user import User
from .. import db
from ..utils.jwt_utils import encoding_token
from ..utils.validators import validate_signup

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json
    error = validate_signup(data)
    if error:
        return {'error': error}, 400
    
    user = User(username=data['username'], email=data['email'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()

    token = encoding_token(user.id)
    return {'message': 'User created', 'token': token}, 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if user and user.check_password(data['password']):
        token = encoding_token(user.id)
        return {'token': token}, 200
    return {'error': 'Invalid credentials'}, 401
