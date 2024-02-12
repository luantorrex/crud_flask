import pytest
from app import create_app, db

@pytest.fixture()
def app():
    """Instance of main app"""
    app = create_app("sqlite://")

    with app.app_context():
        db.create_all()
    
    yield app

@pytest.fixture()
def client(app):
    """Client to use at tests"""
    return app.test_client()