from flask import Flask
from flask_cors import CORS
from app.extensions import db, migrate, jwt, cors, configure_jwt

def create_app():
    """Application factory function"""
    app = Flask(__name__, instance_relative_config=True)
    

    app.config.from_object('app.config.Config')
    
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    CORS(
        app,
        resources={
            r"/*": {
                "origins": [
                    "http://127.0.0.1:5173", 
                    "http://localhost:5173",
                    "https://non-communicable-diseases-charity-api.onrender.com",
                    "https://non-communicable-diseases-charity.onrender.com"
                ],
                "methods": ["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"],
                "allow_headers": ["Content-Type", "Authorization"],
                "supports_credentials": True
            }
        }
    )
    
    configure_jwt(app)
    
    register_blueprints(app)
    
    @app.after_request
    def after_request(response):
        response.headers.add("Access-Control-Allow-Credentials", "true")
        return response
    
    return app

def register_blueprints(app):
    """Register all blueprints with the app"""
    from app.routes.auth_routes import auth_bp
    from app.routes.user_routes import user_bp
    from app.routes.case_routes import case_bp
    from app.routes.donation_routes import donation_bp
    from app.routes.resource_routes import resource_bp
    from app.routes.disease_routes import disease_bp
    from app.routes.area_routes import area_bp
    from app.routes.review_routes import review_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(case_bp)
    app.register_blueprint(donation_bp)
    app.register_blueprint(resource_bp)
    app.register_blueprint(disease_bp)
    app.register_blueprint(area_bp)
    app.register_blueprint(review_bp)
    
    @app.route('/')
    def index():
        return {'message': 'Non-Communicable Diseases Charity API'}, 200
    
    @app.route('/health')
    def health_check():
        return {"status": "healthy"}, 200