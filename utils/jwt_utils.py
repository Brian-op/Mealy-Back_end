import jwt
from jwt import InvalidTokenError
from datetime import datetime  
from flask import current_app

def encoding_token (user_id):
    payload = {
    'exp' : datetime.datetime.utcnow()+ datetime.timedelta(hours=24),
    'iat': datetime.datetime.utcnow(),
    'sub': user_id
    }
    return jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')

def decode_token(token):
    try : 
        payload =jwt.decode(token,current_app.config['SECRET_KEY'],algorithms=['HS256'])
        return payload['sub']

    except jwt.ExpiredSignatureError:
        return None
    except InvalidTokenError:
        return None