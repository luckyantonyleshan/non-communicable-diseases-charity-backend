from flask import Flask
from .extensions import db, migrate, jwt
from .config import Config
from .routes.auth_routes import auth_bp
from .routes.user_routes import user_bp
from .routes.case_routes import case_bp
from .routes.donation_routes import donation_bp
from .routes.resource_routes import resource_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(case_bp)
    app.register_blueprint(donation_bp)
    app.register_blueprint(resource_bp)

    return app
