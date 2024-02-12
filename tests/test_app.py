from app.models import User
import json

def test_app_is_created(app):
    assert app.name == 'app'

def test_debug_is_false(app):
    assert app.config['DEBUG'] is False

def test_404_request(client):
    assert client.get("/page_that_doesnt_exists").status_code == 404

def test_register_user(app, client):
    
    response = client.post(
        "/users/",
        data = json.dumps({"email": "test.test@test.com", "username": "Test Test"})
    )

    with app.app_context():
        assert User.query.count() > 0
