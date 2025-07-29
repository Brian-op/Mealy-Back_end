from flask import Blueprint, request, jsonify
from mealy.models.order import Order
from mealy import db

order_bp = Blueprint('orders', __name__, url_prefix='/orders')

@order_bp.route('/', methods=['GET'])

def get_orders():
    orders = Order.query.all()
    return jsonify([order.to_dict() for order in orders]), 200

@order_bp.route('/<int:order_id>', methods=['GET'])

def get_order_by_id(order_id):
    order = Order.query.get(order_id)

    if not order:
        return jsonify({'error': 'Order not found'}), 404
    return jsonify(order.to_dict())


@order_bp.route('/', methods=['POST'])

def create_order():
    data = request.get_json()
    order = Order(
        user_id=data.get('user_id'),
        meal_id=data.get('meal_id'),
        quantity=data.get('quantity')
    )

    db.session.add(order)
    db.session.commit()
    return jsonify(order.to_dict()), 201

@order_bp.route('/<int:order_id>', methods=['PUT'])

def update_order(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({'error': 'Order not found'}), 404

    data = request.get_json()
    order.quantity = data.get('quantity', order.quantity)

    db.session.commit()
    return jsonify(order.to_dict()), 200

@order_bp.route('/<int:order_id>', methods=['DELETE'])

def delete_order(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({'error': 'Order not found'}), 404

    db.session.delete(order)
    db.session.commit()
    
    return jsonify({'message': 'Order successfully deleted'}), 200
