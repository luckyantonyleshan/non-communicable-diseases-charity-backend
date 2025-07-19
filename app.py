from flask import Flask
from app.utilities.config import Config
from app.utilities.extensions import db, migrate, jwt
from app.routes.auth_routes import auth_bp
from app.routes.user_routes import user_bp
from app.routes.case_routes import case_bp
from app.routes.donation_routes import donation_bp
from app.routes.resource_routes import resource_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(user_bp, url_prefix="/users")
    app.register_blueprint(case_bp, url_prefix="/cases")
    app.register_blueprint(donation_bp, url_prefix="/donations")
    app.register_blueprint(resource_bp, url_prefix="/resources")

    @app.route("/")
    def index():
        return {"message": "Non-Communicable Diseases Charity API"}

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
