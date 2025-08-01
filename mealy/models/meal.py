from mealy import db

class Meal(db.Model):
    __tablename__ = 'meals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, nullable=False)


    menu_links = db.relationship('MenuMeal', back_populates='meal', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Meal {self.name}>"
