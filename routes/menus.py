from flask import Blueprint, request
from controllers.menu_controller import get_menus, get_menu_by_id, create_menu, update_menu, delete_menu

menu_bp = Blueprint('menus', __name__)

@menu_bp.route('/menus', methods=['GET'])
def list_menus():
    return get_menus()

@menu_bp.route('/menus/<int:menu_id>', methods=['GET'])
def get_menu(menu_id):
    return get_menu_by_id(menu_id)

@menu_bp.route('/menus', methods=['POST'])
def add_menu():
    return create_menu(request)

@menu_bp.route('/menus/<int:menu_id>', methods=['PUT'])
def edit_menu(menu_id):
    return update_menu(menu_id, request)

@menu_bp.route('/menus/<int:menu_id>', methods=['DELETE'])
def remove_menu(menu_id):
    return delete_menu(menu_id)
