from flask import Blueprint
from app.routes.auth_routes import auth_bp
from app.routes.user_routes import user_bp
from app.routes.case_routes import case_bp
from app.routes.area_routes import area_bp
from app.routes.review_routes import review_bp
from app.routes.donation_routes import donation_bp
from app.routes.disease_routes import disease_bp
from app.routes.resource_routes import resource_bp
from app.routes.admin_routes import admin_bp


def register_routes(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(case_bp)
    app.register_blueprint(area_bp)
    app.register_blueprint(review_bp)
    app.register_blueprint(donation_bp)
    app.register_blueprint(disease_bp)
    app.register_blueprint(resource_bp)
    app.register_blueprint(admin_bp)