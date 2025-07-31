from flask import Flask
from flask_cors import CORS
from app.extensions import db, migrate, jwt, cors, configure_jwt

def create_app():
    """Application factory function"""
    app = Flask(__name__, instance_relative_config=True)
    
    # Load configuration
    app.config.from_object('app.config.Config')
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    cors.init_app(app)
    
    # Configure JWT after initialization
    configure_jwt(app)
    
    # Register blueprints
    register_blueprints(app)
    
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
