from flask import Blueprint, request, jsonify
from mealy.models.menu import Menu
from mealy import db

menu_bp = Blueprint('menus', __name__, url_prefix='/menus')

@menu_bp.route('/', methods=['GET'])

def get_menus():
    menus = Menu.query.all()
    return jsonify([menu.to_dict() for menu in menus]), 200

@menu_bp.route('/<int:menu_id>', methods=['GET'])

def get_menu_by_id(menu_id):
    menu = Menu.query.get(menu_id)

    if not menu:
        return jsonify({'error': 'Menu not found'}), 404
    
    return jsonify(menu.to_dict())

@menu_bp.route('/', methods=['POST'])

def create_menu():
    data = request.get_json()
    menu = Menu(
        title=data.get('title'),
        date=data.get('date')
    )

    db.session.add(menu)
    db.session.commit()

    return jsonify(menu.to_dict()), 201

@menu_bp.route('/<int:menu_id>', methods=['PUT'])

def update_menu(menu_id):
    menu = Menu.query.get(menu_id)
    if not menu:
        return jsonify({'error': 'Menu not found'}), 404

    data = request.get_json()
    menu.title = data.get('title', menu.title)
    menu.date = data.get('date', menu.date)

    db.session.commit()
    return jsonify(menu.to_dict())

@menu_bp.route('/<int:menu_id>', methods=['DELETE'])

def delete_menu(menu_id):
    menu = Menu.query.get(menu_id)
    if not menu:
        return jsonify({'error': 'Menu not found'}), 404

    db.session.delete(menu)
    db.session.commit()
    
    return jsonify({'message': 'Menu successfully deleted'}), 200
