def validate_signup(data):
    required = ['username', 'email', 'password',]
    for field in required:
        if field not in data or not data[field].strip():
            return f'{field} is required'
    return None