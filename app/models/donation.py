from app.extensions import db

class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    donor_name = db.Column(db.String(100), nullable=False)
    cases = db.relationship("Case", secondary="donation_case", back_populates="donations")
