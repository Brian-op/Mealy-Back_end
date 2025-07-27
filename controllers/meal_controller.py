from flask import jsonify, request, Blueprint
from models.meal import Meal
from models import db  

meal_bp = Blueprint('meals', __name__, url_prefix='/meals')


@meal_bp.route('/', methods=['GET'])

def get_meals():
    meals = Meal.query.all()
    return jsonify([meal.to_dict() for meal in meals]), 200


@meal_bp.route('/<int:meal_id>', methods=['GET'])

def get_meal_by_id(meal_id):
    meal = Meal.query.get(meal_id)

    if not meal:
        return jsonify({'error': 'Meal not found'}), 404
    return jsonify(meal.to_dict()), 200


@meal_bp.route('/', methods=['POST'])

def create_meal():
    data = request.get_json()
    meal = Meal(
        name=data['name'],
        price=data['price'],
        description=data.get('description')
    )

    db.session.add(meal)
    db.session.commit()
    return jsonify(meal.to_dict())


@meal_bp.route('/<int:meal_id>', methods=['PUT'])

def update_meal(meal_id):
    meal = Meal.query.get(meal_id)

    if not meal:
        return jsonify({'error': 'Meal not found'}), 404
    
    data = request.get_json()
    meal.name = data.get('name', meal.name)
    meal.price = data.get('price', meal.price)
    meal.description = data.get('description', meal.description)

    db.session.commit()
    return jsonify(meal.to_dict()), 200


@meal_bp.route('/<int:meal_id>', methods=['DELETE'])

def delete_meal(meal_id):
    meal = Meal.query.get(meal_id)
    if not meal:
        return jsonify({'error': 'Meal not found'}), 404

    db.session.delete(meal)
    db.session.commit()
    return jsonify({'Message': 'Meal successfully deleted'})
