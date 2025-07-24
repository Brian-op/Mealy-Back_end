from flask import Blueprint, request
from controllers.order_controller import get_orders, get_order_by_id, create_order, update_order, delete_order

order_bp = Blueprint('orders', __name__)

@order_bp.route('/orders', methods=['GET'])
def list_orders():
    return get_orders()

@order_bp.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    return get_order_by_id(order_id)

@order_bp.route('/orders', methods=['POST'])
def add_order():
    return create_order(request)

@order_bp.route('/orders/<int:order_id>', methods=['PUT'])
def edit_order(order_id):
    return update_order(order_id, request)

@order_bp.route('/orders/<int:order_id>', methods=['DELETE'])
def remove_order(order_id):
    return delete_order(order_id)
