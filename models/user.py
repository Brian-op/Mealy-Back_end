from .. import db
from werkzeug.security import generate_password_hash, check_password_hash

class User (db.Model):
    __tablename__= 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    role = db.Column(db.String(20), default='customer')  # or 'admin'

    def is_admin(self):
        return self.role == 'admin'

    orders = db.relationship('Order', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def password_check(self, password):
        return check_password_hash(self.password_hash, password)
