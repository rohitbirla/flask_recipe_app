# Flask Recipe App
This is a Flask-based web application for managing recipes. Users can register, log in, add, edit, and delete recipes. Each recipe includes a title, description, list of ingredients, and cooking instructions. The application uses SQLAlchemy for database management and Flask-Login for user authentication.

# Features
- User Management:

- User registration and login.
- Authentication with Flask-Login.
- User-specific recipe management.
  
# Recipe Management:

- Create, edit, and delete recipes.
- Each recipe includes a title, description, ingredients, and instructions.
- Search recipes by title or ingredients.

# Technologies Used
- Flask: Python web framework used for building the application.
- SQLAlchemy: SQL toolkit and Object-Relational Mapping (ORM) for database management.
- Flask-Login: Provides user session management for Flask applications.
- Bootstrap: Front-end framework for responsive and mobile-first web development.

# Setup Instructions
To run this application locally, follow these steps:

1. Clone the repository:

`git clone https://github.com/your_username/flask-recipe-app.git`
`cd flask-recipe-app`

2. Install dependencies:
It's recommended to use a virtual environment (e.g., venv) to manage dependencies.

`python -m venv venv`
`. venv/bin/activate`  # On Windows, use `venv\Scripts\activate`
`pip install -r requirements.txt`

3. Set up the database:
Ensure you have SQLite installed locally. Initialize the database with the following commands:

python
>>> from app import db
>>> db.create_all()
>>> exit()
Run the application:

bash
Copy code
flask run
The application should now be accessible at http://localhost:5000.
