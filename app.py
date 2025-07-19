from flask import Flask
import app.config
import app.extensions
import app.routes.auth_routes
import app.routes.user_routes
import app.routes.case_routes
import app.routes.donation_routes
import app.routes.resource_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(app.config.Config)

    app.extensions.db.init_app(app)
    app.extensions.migrate.init_app(app, app.extensions.db)
    app.extensions.jwt.init_app(app)

    app.register_blueprint(app.routes.auth_routes.auth_bp, url_prefix="/auth")
    app.register_blueprint(app.routes.user_routes.user_bp, url_prefix="/users")
    app.register_blueprint(app.routes.case_routes.case_bp, url_prefix="/cases")
    app.register_blueprint(app.routes.donation_routes.donation_bp, url_prefix="/donations")
    app.register_blueprint(app.routes.resource_routes.resource_bp, url_prefix="/resources")

    @app.route("/")
    def index():
        return {"message": "Non-Communicable Diseases Charity API"}

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)