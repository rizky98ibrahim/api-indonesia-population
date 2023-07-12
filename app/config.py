import os
from dotenv import load_dotenv

# Environment Variables
load_dotenv()

# Flask Configuration
DEBUG = True
SECRET_KEY = os.getenv("SECRET_KEY")

# SQLAlchemy Configuration
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
SQLALCHEMY_TRACK_MODIFICATIONS = False