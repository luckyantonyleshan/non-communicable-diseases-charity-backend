from flask import Flask
from flask_cors import CORS
from app.extensions import db, migrate, jwt, cors
from flask_admin import Admin

admin = Admin()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('app.config.Config')

    # Initialize CORS
    CORS(app, resources={
        r"/*": {
            "origins": ["http://127.0.0.1:5173", "http://localhost:5173", 
                       "https://non-communicable-diseases-charity-api.onrender.com"],
            "methods": ["GET", "POST", "PUT", "DELETE"],
            "allow_headers": ["Content-Type", "Authorization"]
        }
    })

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    cors.init_app(app)
    admin.init_app(app)

    # Import and register blueprints
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

    # Configure JWT
    from app.extensions import configure_jwt
    configure_jwt(app)

    @app.route("/")
    def index():
        return {"message": "Non-Communicable Diseases Charity API"}

    return app