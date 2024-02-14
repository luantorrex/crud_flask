from flask import (
    Blueprint,
    jsonify,
    make_response,
    request
)
from .models import db, User
from controllers.user import (
    format_request_data,
    get_user_by_id
)

users_bp = Blueprint('users', __name__)

@users_bp.route('/', methods=['GET'])
def get_users() -> str:
    """
    Gets every row from the database.

    :returns: str
    """
    users_table = User.query.all()
    users_json = [user_.to_json() for user_ in users_table]

    return make_response(
        jsonify(
            message='Listing all users.',
            data=users_json
        ), 200
    )

@users_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id: int) -> str:
    """
    Gets a specific user by its id.

    :param user_id: Integer to index a user at the database.

    :returns: str
    """
    user = get_user_by_id(user_id)
    user_json = user.to_json()

    return make_response(
        jsonify(
            message=f'Listing user with id {user_id}.',
            data=user_json
        ), 200
    )

@users_bp.route('/', methods=['POST'])
def add_user():
    """
    Inserts a new user at the database.

    :returns: str
    """
    request_data = format_request_data(request)

    obligatory_fields = ['username', 'email']

    for obligatory_field in obligatory_fields:
        if not request_data.get(obligatory_field):
            return make_response(
                jsonify(
                    message=f'{obligatory_field} is an obligatory field, please provide it.'
                ), 400
            )

    user = User(username=request_data['username'], email=request_data['email'])

    if User.query.filter_by(email=user.email).first():
        return make_response(
            jsonify(
                message='User already exists at database.'
            ), 400
        )

    db.session.add(user)
    db.session.commit()

    user = User.query.filter_by(email=request_data['email']).first()
    user_json = user.to_json()

    return make_response(
        jsonify(
            message='User created with success.',
            data=user_json
        ), 200
    )

@users_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Update a row at the database.

    :params int user_id: Integer to index a user at the database.
    :returns: str
    """
    request_data = format_request_data(request)
    user = get_user_by_id(user_id)

    if request_data.get('username'):
        user.username = request_data['username']

    if request_data.get('email'):
        user.email = request_data['email']

    db.session.commit()

    user = get_user_by_id(user_id)
    user_json = user.to_json()

    return make_response(
        jsonify(
            message=f'User with id {user_id} updated with success.',
            data=user_json
        ), 200
    )

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

    return make_response(
        jsonify(
            message=f'User with id {user_id} has been deleted.'
        ), 200
    )

@users_bp.app_errorhandler(400)
def errors_400(e):
    """
    In case of not receiving any obligatory field.
    """
    return make_response(
        jsonify(
            message='Bad Request.'
        ), 400
    )

@users_bp.app_errorhandler(404)
def errors_404(e):
    """
    In case of not finding a specific user.
    """
    return make_response(
        jsonify(
            message='Not Found.'
        ), 404
    )

@users_bp.app_errorhandler(500)
def errors_500(e):
    """
    Internal server error.
    """
    return make_response(
        jsonify(
            message='Internal Server Error.'
        ), 500
    )
