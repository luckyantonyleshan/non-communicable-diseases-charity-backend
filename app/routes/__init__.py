from .auth_routes import auth_bp
from .case_routes import case_bp
from .donation_routes import donation_bp
from .resource_routes import resource_bp
from .user_routes import user_bp

def register_routes(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(case_bp)
    app.register_blueprint(donation_bp)
    app.register_blueprint(resource_bp)
