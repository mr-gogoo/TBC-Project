from ext import db  # Import the db object
from app import app  # Import your Flask app
from models import User, Item

# Ensure the Flask app context is pushed for database operations
with app.app_context():
    # Option 1: Drop the `users` table
    User.__table__.drop(db.engine)

    # Option 2: Execute raw SQL
    # db.engine.execute("DROP TABLE IF EXISTS users;")

    print("The 'users' table has been deleted.")
