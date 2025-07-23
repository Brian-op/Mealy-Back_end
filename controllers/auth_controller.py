from models.user import User, db
from utils.jwt_utils import encoding_token
from utils.validators import validate_signup

def signup(data):
    error = validate_signup(data)
    if error:
        return{'error':error},400
    
    user = User(username = data['username'], email= data['email'])
    user.set_password(data['password'])
    
    db.session.add(user)
    db.session.commit()

    token = encoding_token(user.id)
    return {'message': 'User created', 'token': {token}},201

def login (data):
    user= User.query.filter_by(email=data['email']).first()

    if user and user.check_password(data['password']):
        token= encoding_token(user.id)
        return {'token':token},200
    return{'error': 'Invalid credentials'},401