from flask import Flask
from app.extensions import db, migrate, jwt, cors
from app.config import Config

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    cors.init_app(app)

    from app.models.user import User
    from app.models.case import Case
    from app.models.donation import Donation
    from app.models.resource import Resource

    from app.routes import register_routes
    register_routes(app)

    return app