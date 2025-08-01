from mealy import db
from datetime import datetime

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    menu_meal_id = db.Column(db.Integer, db.ForeignKey('menu_meals.id'), nullable=False)
    quantity = db.Column(db.Integer, default=1, nullable=False)
    status = db.Column(db.String(50), default='pending', nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    user = db.relationship('User', back_populates='orders')
    menu_meal = db.relationship('MenuMeal', back_populates='orders')

    def __repr__(self):
        return f"<Order User={self.user_id} Meal={self.menu_meal_id} Qty={self.quantity}>"
