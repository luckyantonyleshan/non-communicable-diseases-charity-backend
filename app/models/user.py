import app.extensions
from werkzeug.security import generate_password_hash, check_password_hash

class User(app.extensions.db.Model):
    id = app.extensions.db.Column(app.extensions.db.Integer, primary_key=True)
    username = app.extensions.db.Column(app.extensions.db.String(80), unique=True, nullable=False)
    email = app.extensions.db.Column(app.extensions.db.String(120), unique=True, nullable=False)
    password_hash = app.extensions.db.Column(app.extensions.db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)