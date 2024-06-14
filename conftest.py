# conftest.py

import pytest
from flask import Flask
from app import db  # Adjust to import db from your actual module

# Fixture to initialize Flask app with SQLAlchemy for testing
@pytest.fixture(scope='session')
def app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    # Initialize SQLAlchemy with the Flask app context
    with app.app_context():
        db.init_app(app)
        db.create_all()  # Create all tables based on defined models
        yield app

    # Teardown - remove the database session and tables if needed
    with app.app_context():
        db.drop_all()

@pytest.fixture(scope='session')
def client(app):
    return app.test_client()

# Add more fixtures as needed for your tests
