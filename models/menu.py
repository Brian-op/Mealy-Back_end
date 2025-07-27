from .. import db
from datetime import date

class Menu(db.Model):
    __tablename__ = "menus"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=date.today, unique=True, nullable=False)

    meals = db.relationship('MenuMeal', backref='menu', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "date": str(self.date),
            "meals": [menu_meal.meal.to_dict() for menu_meal in self.meals]
        }
