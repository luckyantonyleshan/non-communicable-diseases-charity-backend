from flask import Flask
from .config import Config
from .extensions import db, migrate, jwt

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    from .routes.auth_routes import auth_bp
    from .routes.user_routes import user_bp
    from .routes.case_routes import case_bp
    from .routes.donation_routes import donation_bp
    from .routes.resource_routes import resource_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(user_bp, url_prefix="/users")
    app.register_blueprint(case_bp, url_prefix="/cases")
    app.register_blueprint(donation_bp, url_prefix="/donations")
    app.register_blueprint(resource_bp, url_prefix="/resources")

    @app.route("/")
    def index():
        return {"message": "Non-Communicable Diseases Charity API"}

    return app