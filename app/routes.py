from flask import Blueprint, request, jsonify, make_response
from .models import db, User
import json

users_bp = Blueprint('users', __name__)

@users_bp.route('/', methods=['GET'])
def get_users():
    users_table = User.query.all()
    users_list = []

    for user in users_table:
        user_row = {k: v for k, v in user.__dict__.items() if k != '_sa_instance_state'}
        users_list.append(user_row)

    return make_response(jsonify(users_list), 200)

@users_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()

    if not user:
        return make_response(
            jsonify({'msg': f'User with id {user_id} not found.'}),
            404
        )        

    user_row = {k: v for k, v in user.__dict__.items() if k != '_sa_instance_state'}

    return make_response(jsonify(user_row), 200)

@users_bp.route('/', methods=['POST'])
def add_user():
    request_data = json.loads(request.data.decode().replace("'", '"'))
    user = User(username=request_data['username'], email=request_data['email'])

    db.session.add(user)
    db.session.commit()

    user = User.query.filter_by(email=request_data['email']).first()
    user_row = {k: v for k, v in user.__dict__.items() if k != '_sa_instance_state'}

    return make_response(jsonify(user_row), 200)

@users_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    request_data = json.loads(request.data.decode().replace("'", '"'))
    user = User.query.filter_by(id=user_id).first()

    user.username = request_data['username']
    user.email = request_data['email']

    db.session.commit()

    user = User.query.filter_by(id=user_id).first()
    user_row = {k: v for k, v in user.__dict__.items() if k != '_sa_instance_state'}

    return make_response(jsonify(user_row), 200)

@users_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()

    db.session.delete(user)
    db.session.commit()    

    return make_response(jsonify({
        'msg': f'User with id {user_id} has been deleted.'
    }), 200)

@users_bp.app_errorhandler(404)
def errors_404(e):
    return make_response(jsonify({
        'msg': 'Error 404'
    }), 404)

@users_bp.app_errorhandler(500)
def errors_500(e):
    return make_response(jsonify({
        'msg': 'Internal Server Error'
    }), 500)
