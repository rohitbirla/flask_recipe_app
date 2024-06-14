# test_app.py

import pytest
from app import app, db, User, Recipe
from flask_login import login_user, logout_user, current_user



def test_login(client):
    # Create a test user
    user = User(username='testuser', password='testpassword')
    db.session.add(user)
    db.session.commit()

    # Attempt to login with correct credentials
    response = client.post('/login', data=dict(
        username='testuser',
        password='testpassword'
    ), follow_redirects=True)
    assert b'You have been logged in.' in response.data
    assert current_user.username == 'testuser'

def test_logout(client):
    # Login the user first
    test_login(client)

    # Logout the user
    response = client.get('/logout', follow_redirects=True)
    assert b'You have been logged out.' in response.data
    assert not current_user.is_authenticated

def test_add_recipe(client):
    # Create a test user
    user = User(username='testuser', password='testpassword')
    db.session.add(user)
    db.session.commit()

    # Login the user
    with client:
        client.post('/login', data=dict(
            username='testuser',
            password='testpassword'
        ), follow_redirects=True)

        # Add a recipe via POST request
        response = client.post('/recipes/new', data=dict(
            title='New Recipe',
            description='Description of new recipe',
            ingredients='Ingredients for new recipe',
            instructions='Instructions for new recipe'
        ), follow_redirects=True)

        # Check if the recipe was added successfully
        assert b'Recipe added successfully!' in response.data

        # Check if the recipe exists in the database
        recipe = Recipe.query.filter_by(title='New Recipe').first()
        assert recipe is not None

def test_delete_recipe(client):
    # Create a test user
    user = User(username='testuser', password='testpassword')
    db.session.add(user)
    db.session.commit()

    # Create a recipe to delete
    new_recipe = Recipe(title='Recipe to delete', description='Description', ingredients='Ingredients', instructions='Instructions', created_by=user.id)
    db.session.add(new_recipe)
    db.session.commit()

    # Login the user
    with client:
        client.post('/login', data=dict(
            username='testuser',
            password='testpassword'
        ), follow_redirects=True)

        # Delete the recipe via POST request
        response = client.post(f'/recipes/{new_recipe.id}/delete', follow_redirects=True)

        # Check if the recipe was deleted successfully
        assert b'Recipe deleted successfully!' in response.data

        # Check if the recipe no longer exists in the database
        recipe = Recipe.query.filter_by(title='Recipe to delete').first()
        assert recipe is None
