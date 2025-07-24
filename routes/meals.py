from flask import Blueprint, request
from controllers.meal_controller import get_meals, get_meal_by_id, create_meal, update_meal, delete_meal

meal_bp = Blueprint('meals', __name__)

@meal_bp.route('/meals', methods=['GET'])
def list_meals():
    return get_meals()

@meal_bp.route('/meals/<int:meal_id>', methods=['GET'])
def get_meal(meal_id):
    return get_meal_by_id(meal_id)

@meal_bp.route('/meals', methods=['POST'])
def add_meal():
    return create_meal(request)

@meal_bp.route('/meals/<int:meal_id>', methods=['PUT'])
def edit_meal(meal_id):
    return update_meal(meal_id, request)

@meal_bp.route('/meals/<int:meal_id>', methods=['DELETE'])
def remove_meal(meal_id):
    return delete_meal(meal_id)
