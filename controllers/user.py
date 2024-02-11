from app.models import db, User
from flask import abort, Request
import json

def format_user_data(user: User) -> dict:
    """
    Formats user data

    :param User user: User object

    :returns: dict
    """
    return {k: v for k, v in user.__dict__.items() if k != '_sa_instance_state'}

def get_user_by_id(user_id:int) -> User:
    """
    Gets a specific user by its id. If not found, raises 404 status code.

    :returns: User
    """
    user = User.query.filter_by(id=user_id).first()

    if not user:
        abort(404)

    return user

def format_request_data(request:Request) -> dict:
    """
    Formats the data request, casting it from bytes to json.

    In case of missing username or email (obligatory fields), 
    it returns a 400 code to the request.

    :params Request request: Received request
    :returns: dict
    """
    request_data = json.loads(request.data.decode().replace("'", '"'))

    if not request_data['username'] or not request_data['email']:
        abort(400)

    return request_data
