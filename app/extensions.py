from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
cors = CORS(resources={
    r"/*": {
        "origins": ["http://127.0.0.1:5173", "http://localhost:5173", "https://non-communicable-diseases-charity-api.onrender.com"],
        "methods": ["GET", "POST", "PUT", "DELETE"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

def configure_jwt(app):
    from app.models.user import User  # Lazy import
    @jwt.user_identity_loader
    def user_identity_lookup(identity):
        return str(identity)  # Return identity as string (handles integer ID)

    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        return User.query.get(int(identity))  # Convert string to int for query