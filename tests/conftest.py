import os
import pytest
import sys

from flask import current_app

app_dir = os.path.abspath(os.path.join(os.getcwd(), "app"))
sys.path.append(app_dir)
sys.path.append(os.getcwd())

from server import create_app, db
from server.models.user import User


@pytest.fixture(scope='module')
def test_request_context():
    flask_app = create_app()

    # can be used in combination with the WITH statement to activate a request context temporarily.
    # with this you can access the request, g and session objects in view functions
    yield flask_app.test_request_context


@pytest.fixture(scope='module')
def create_testing_client():
    flask_app = create_app()

    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = flask_app.test_client()

    # Establish an application context before running the tests.
    context = flask_app.app_context()
    context.push()

    yield testing_client  # this is where the testing happens!

    context.pop()


@pytest.fixture(scope='module')
def initialize_database():
    # Create the database and the database table

    with current_app.app_context():
        db.create_all()

    yield db  # this is where the testing happens!

    with current_app.app_context():
        db.session.remove()  # DO NOT DELETE THIS LINE. We need to close sessions before dropping tables.
        db.drop_all()


@pytest.fixture(scope='module')
def create_user(create_testing_client, initialize_database):
    user = User(first_name='Test',
                secomd_name='User')

    db.session.commit()
    return user
