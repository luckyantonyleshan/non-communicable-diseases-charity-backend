from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix
from app import create_app
# from app.seed import run_seed 

app = create_app()
# run_seed(seed.py)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000, debug=True)

# from flask import Flask
# from app.config import Config
# from app.extensions import db, migrate, jwt, cors

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(Config)

#     # Initialize extensions
#     db.init_app(app)
#     migrate.init_app(app, db)
#     jwt.init_app(app)
#     cors.init_app(app)

#     # Import and register blueprints
#     from app.routes.auth_routes import auth_bp
#     from app.routes.user_routes import user_bp
#     from app.routes.case_routes import case_bp
#     from app.routes.donation_routes import donation_bp
#     from app.routes.resource_routes import resource_bp

#     app.register_blueprint(auth_bp, url_prefix="/auth")
#     app.register_blueprint(user_bp, url_prefix="/users")
#     app.register_blueprint(case_bp, url_prefix="/cases")
#     app.register_blueprint(donation_bp, url_prefix="/donations")
#     app.register_blueprint(resource_bp, url_prefix="/resources")

#     @app.route("/")
#     def index():
#         return {"message": "Non-Communicable Diseases Charity API"}

#     return app

# if __name__ == "__main__":
#     app = create_app()
#     app.run(debug=True)