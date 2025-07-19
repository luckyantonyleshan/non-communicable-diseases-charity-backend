import app.extensions

class Resource(app.extensions.db.Model):
    id = app.extensions.db.Column(app.extensions.db.Integer, primary_key=True)
    title = app.extensions.db.Column(app.extensions.db.String(120), nullable=False)
    url = app.extensions.db.Column(app.extensions.db.String(200), nullable=False)