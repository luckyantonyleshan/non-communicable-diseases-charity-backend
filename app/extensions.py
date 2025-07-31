# app/extensions.py
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
cors = CORS(resources={
    r"/*": {
        "origins": ["http://127.0.0.1:5173", "http://localhost:5173", 
                   "https://non-communicable-diseases-charity-api.onrender.com"],
        "methods": ["GET", "POST", "PUT", "DELETE"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

def configure_jwt(app):
    from app.models.user import User
    
    @jwt.user_identity_loader
    def user_identity_lookup(user):
        # Return just the user ID as identity
        return user.id if isinstance(user, User) else user.get('id')
    
    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        # Handle both dictionary and integer identities
        if isinstance(identity, dict):
            return User.query.get(identity.get('id'))
        return User.query.get(identity)