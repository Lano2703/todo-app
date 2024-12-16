# app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create the database object (this will be imported by models.py)
db = SQLAlchemy()

# App factory function
def create_app():
    app = Flask(__name__)  # Create the Flask app instance
    app.config.from_object('config.Config')  # Load config settings from config.py
    db.init_app(app)  # Initialize the db with the app
    return app
