from app.extensions import db
from app.models.association import donation_case

class Donation(db.Model):
    __tablename__ = "donations"

    id = db.Column(db.Integer, primary_key=True)
    donor_name = db.Column(db.String(120), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  
    case_id = db.Column(db.Integer, db.ForeignKey("cases.id"))

    cases = db.relationship("Case", secondary=donation_case, back_populates="donations")