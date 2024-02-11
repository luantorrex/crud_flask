from flask import Blueprint, request, jsonify
from .models import db, User

users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['GET'])
def get_users():
    pass

@users_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    pass

@users_bp.route('/users', methods=['POST'])
def add_user():
    pass

@users_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    pass

@users_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    pass
