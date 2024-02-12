import pytest
from app import create_app
from app.database import db

@pytest.fixture(scope="module")
def app():
    """Instance of main app"""
    return create_app("sqlite://")
