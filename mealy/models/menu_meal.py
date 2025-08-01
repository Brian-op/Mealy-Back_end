from mealy import db

class MenuMeal(db.Model):
    __tablename__ = 'menu_meals'

    id = db.Column(db.Integer, primary_key=True)
    menu_id = db.Column(db.Integer, db.ForeignKey('menus.id'), nullable=False)
    meal_id = db.Column(db.Integer, db.ForeignKey('meals.id'), nullable=False)

  
    meal = db.relationship('Meal', back_populates='menu_links')
    menu = db.relationship('Menu', back_populates='meal_links')
    orders = db.relationship('Order', back_populates='menu_meal', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<MenuMeal Menu={self.menu_id} Meal={self.meal_id}>"
