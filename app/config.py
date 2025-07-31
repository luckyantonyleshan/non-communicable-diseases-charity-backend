import os
from urllib.parse import quote_plus
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Database configuration with proper error handling
    try:
        DB_URI = os.environ['DATABASE_URI']
        if DB_URI.startswith('postgres://'):
            DB_URI = DB_URI.replace('postgres://', 'postgresql://', 1)
        
        # Handle password special characters
        if '@' in DB_URI:
            parts = DB_URI.split('@')
            auth_part = parts[0]
            if ':' in auth_part:
                user_pass = auth_part.split('://')[1]
                user, password = user_pass.split(':')
                encoded_password = quote_plus(password)
                DB_URI = DB_URI.replace(f':{password}', f':{encoded_password}')
        
        SQLALCHEMY_DATABASE_URI = DB_URI
    except KeyError:
        if os.environ.get('RENDER'):
            raise RuntimeError("DATABASE_URI must be set in production")
        SQLALCHEMY_DATABASE_URI = 'sqlite:///instance/dev.db'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback-secret-key-for-development-only')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', SECRET_KEY)  # Use SECRET_KEY as fallback