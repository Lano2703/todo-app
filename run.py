# run.py

from app import create_app, db
from models import Todo  # Import the Todo model to ensure it's registered with the database

# Create the app instance
app = create_app()

# Create all tables (this will create the tables in your PostgreSQL database)
with app.app_context():
    db.create_all()  # This will create the tables based on your models

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
