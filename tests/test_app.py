from app.models import User
import json

def test_app_is_created(app):
    assert app.name == 'app'

def test_debug_is_false(app):
    assert app.config['DEBUG'] is False

def test_404_request(client):
    assert client.get("/page_that_doesnt_exists").status_code == 404

def test_if_database_count_raises_with_a_correct_insert(app, client):
    with app.app_context():
        previous_cont = User.query.count()

        response = client.post(
            "/users/",
            data = json.dumps({
                "email": "test.test@test.com",
                "username": "Test Test"
            })
        )

        if response.status_code == 200:
            assert User.query.count() > previous_cont

def test_if_database_cont_changes_with_an_incorrent_insert(app, client):
    with app.app_context():
        previous_cont = User.query.count()

        client.post(
            "/users/incorrect_url",
            data = json.dumps({'':''})
        )

        assert User.query.count() == previous_cont

def test_if_a_user_was_correctly_inserted(app, client):
    response = client.post(
        "/users/",
        data = json.dumps({"email": "test.test@test.com", "username": "Test Test"})
    )

    with app.app_context():
        assert User.query.filter_by(email="test.test@test.com").count() == 1
        assert response.status_code == 200

def test_get_a_user_that_doesnt_exists(app, client):
    response = client.get(
        "/users/100",
    )

    with app.app_context():
        assert response.status_code == 404
