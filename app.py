from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)




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