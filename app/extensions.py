from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from datetime import timedelta

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
cors = CORS(resources={
    r"/*": {
        "origins": ["http://127.0.0.1:5173", "http://localhost:5173", 
                   "https://non-communicable-diseases-charity-api.onrender.com"],
        "methods": ["GET", "POST", "PUT", "DELETE", "PATCH"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

def configure_jwt(app):
    app.config['JWT_SECRET_KEY'] = app.config['SECRET_KEY']
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=24)
    app.config['JWT_ALGORITHM'] = 'HS256'
    
    @jwt.user_identity_loader
    def user_identity_lookup(user):
        # Return the user ID directly
        return user
    
    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        from app.models.user import User
        identity = jwt_data["sub"]
        return User.query.get(identity)
    
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return {'error': 'Token has expired'}, 401
    
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return {'error': 'Invalid token'}, 422
    
    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return {'error': 'Authorization token is required'}, 401
