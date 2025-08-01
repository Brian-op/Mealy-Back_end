from mealy import db

class Menu(db.Model):
    __tablename__ = 'menus'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)


    meal_links = db.relationship('MenuMeal', back_populates='menu', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Menu {self.name}>"
