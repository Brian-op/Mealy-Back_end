from mealy import db

class MenuMeal(db.Model):
    __tablename__ = "menu_meals"

    id = db.Column(db.Integer, primary_key=True)
    menu_id = db.Column(db.Integer, db.ForeignKey('menus.id'), nullable=False)
    meal_id = db.Column(db.Integer, db.ForeignKey('meals.id'), nullable=False)
