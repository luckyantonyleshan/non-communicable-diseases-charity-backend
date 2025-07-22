import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default-secret-key-for-dev-only")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "default-jwt-secret-for-dev-only")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///instance/db.sqlite3")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True