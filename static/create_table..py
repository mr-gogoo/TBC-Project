from ext import db  # Import the db object
from app import app  # Import your Flask app
from models import User, Item

# Ensure the Flask app context is pushed for database operations
with app.app_context():
    # Create the User table
    User.__table__.create(db.engine)
    print("The 'User' table has been created.")
