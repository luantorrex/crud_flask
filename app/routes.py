from flask import Blueprint, abort, request, jsonify, make_response
from .models import db, User
from controllers.user import (
    format_user_data,
    format_request_data,
    get_user_by_id,
)
import json

users_bp = Blueprint('users', __name__)

@users_bp.route('/', methods=['GET'])
def get_users() -> str:
    """
    Gets every row from the database.

    :returns: str
    """
    users_table = User.query.all()
    users_list = []

    for user in users_table:
        user_data = format_user_data(user)
        users_list.append(user_data)

    return make_response(jsonify(users_list), 200)

@users_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id: int) -> str:
    """
    Gets a specific user by its id.

    :param user_id: Integer to index a user at the database.

    :returns: str
    """
    user = get_user_by_id(user_id)
    user_row = format_user_data(user)

    return make_response(jsonify(user_row), 200)

@users_bp.route('/', methods=['POST'])
def add_user():
    """
    Inserts a new user at the database.

    :returns: str
    """
    request_data = format_request_data(request)

    user = User(username=request_data['username'], email=request_data['email'])

    db.session.add(user)
    db.session.commit()

    user = User.query.filter_by(email=request_data['email']).first()
    user_row = format_user_data(user)

    return make_response(jsonify(user_row), 200)

@users_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Update a row at the database.

    :params int user_id: Integer to index a user at the database.
    :returns: str
    """
    request_data = format_request_data(request)

    user = get_user_by_id(user_id)
    user.username = request_data['username']
    user.email = request_data['email']

    db.session.commit()

    user = get_user_by_id(user_id)
    user_row = format_user_data(user)

    return make_response(jsonify(user_row), 200)

@users_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Deletes a user at the database.
    
    :params int user_id: Integer to index a user at the database.
    :returns: str
    """
    user = get_user_by_id(user_id)

    db.session.delete(user)
    db.session.commit()    

    return make_response(jsonify({
        'msg': f'User with id {user_id} has been deleted.'
    }), 200)

@users_bp.app_errorhandler(400)
def errors_400(e):
    return make_response(jsonify({
        'msg': 'Bad Request'
    }), 400)

@users_bp.app_errorhandler(404)
def errors_404(e):
    return make_response(jsonify({
        'msg': 'Not Found'
    }), 404)

@users_bp.app_errorhandler(500)
def errors_500(e):
    return make_response(jsonify({
        'msg': 'Internal Server Error'
    }), 500)
