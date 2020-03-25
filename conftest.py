from app import app as flask_app
import pytest


@pytest.fixture
def app():
    return flask_app.test_client()
