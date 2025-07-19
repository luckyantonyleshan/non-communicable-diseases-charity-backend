import app.extensions

class Donation(app.extensions.db.Model):
    id = app.extensions.db.Column(app.extensions.db.Integer, primary_key=True)
    amount = app.extensions.db.Column(app.extensions.db.Float, nullable=False)
    donor_name = app.extensions.db.Column(app.extensions.db.String(100), nullable=False)
    user_id = app.extensions.db.Column(app.extensions.db.Integer, app.extensions.db.ForeignKey('user.id'))
    cases = app.extensions.db.relationship("Case", secondary="donation_case", back_populates="donations")