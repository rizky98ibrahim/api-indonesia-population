from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

db = SQLAlchemy()

def create_app():
    
    app = Flask(__name__)
    load_dotenv()
    app.config.from_pyfile("config.py")

    db.init_app(app)
    migrate = Migrate(app, db)

    with app.app_context():
        # Import models
        from app.models.population import Population
        
        # Import and register the blueprint
        from app.routes import bp
        app.register_blueprint(bp)
        
        # Create tables for our models
        db.create_all()
        
        # Return the app
        return app
