import app.extensions

class Case(app.extensions.db.Model):
    id = app.extensions.db.Column(app.extensions.db.Integer, primary_key=True)
    title = app.extensions.db.Column(app.extensions.db.String(100), nullable=False)
    description = app.extensions.db.Column(app.extensions.db.Text, nullable=False)
    user_id = app.extensions.db.Column(app.extensions.db.Integer, app.extensions.db.ForeignKey('user.id'))
    donations = app.extensions.db.relationship("Donation", secondary="donation_case", back_populates="cases")