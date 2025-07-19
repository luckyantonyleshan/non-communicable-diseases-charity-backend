from app.extensions import db

class Case(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    donations = db.relationship("Donation", secondary="donation_case", back_populates="cases")
