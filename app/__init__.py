# from flask import Flask
# from flask_cors import CORS
# from app.extensions import db, migrate, jwt, cors, configure_jwt
# from app.config import Config

# def create_app():
#     app = Flask(__name__, instance_relative_config=True)
#     app.config.from_object(Config)

#     # Initialize CORS with allowed origins
#     CORS(app, resources={
#         r"/*": {
#             "origins": ["http://127.0.0.1:5173", "http://localhost:5173", "https://non-communicable-diseases-charity-api.onrender.com"],
#             "methods": ["GET", "POST", "PUT", "DELETE"],
#             "allow_headers": ["Content-Type", "Authorization"]
#         }
#     })

#     # Initialize extensions
#     db.init_app(app)
#     migrate.init_app(app, db)
#     jwt.init_app(app)
#     cors.init_app(app)

#     # Import models after db initialization
#     with app.app_context():
#         from app.models.user import User
#         from app.models.case import Case
#         from app.models.donation import Donation
#         from app.models.resource import Resource
#         from app.models.disease import Disease
#         from app.models.area import Area
#         from app.models.review import Review

#     # Configure JWT after app and models are ready
#     configure_jwt(app)

#     # Register routes
#     from app.routes.auth_routes import auth_bp
#     from app.routes.user_routes import user_bp
#     from app.routes.case_routes import case_bp
#     from app.routes.donation_routes import donation_bp
#     from app.routes.resource_routes import resource_bp
#     from app.routes.disease_routes import disease_bp
#     from app.routes.area_routes import area_bp
#     from app.routes.review_routes import review_bp

#     app.register_blueprint(auth_bp, url_prefix="/auth")
#     app.register_blueprint(user_bp, url_prefix="/users")
#     app.register_blueprint(case_bp, url_prefix="/cases")
#     app.register_blueprint(donation_bp, url_prefix="/donations")
#     app.register_blueprint(resource_bp, url_prefix="/resources")
#     app.register_blueprint(disease_bp, url_prefix="/diseases")
#     app.register_blueprint(area_bp, url_prefix="/areas")
#     app.register_blueprint(review_bp, url_prefix="/reviews")

#     @app.route("/")
#     def index():
#         return {"message": "Non-Communicable Diseases Charity API"}

#     return app

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

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(user_bp, url_prefix="/users")
    app.register_blueprint(case_bp, url_prefix="/cases")
    app.register_blueprint(donation_bp, url_prefix="/donations")
    app.register_blueprint(resource_bp, url_prefix="/resources")
    app.register_blueprint(disease_bp, url_prefix="/diseases")
    app.register_blueprint(area_bp, url_prefix="/areas")
    app.register_blueprint(review_bp, url_prefix="/reviews")

    # Configure JWT
    from app.extensions import configure_jwt
    configure_jwt(app)

    @app.route("/")
    def index():
        return {"message": "Non-Communicable Diseases Charity API"}

    return app