from app.extensions import db
from app.models.association import donation_case

class Case(db.Model):
    __tablename__ = "cases"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    amount_needed = db.Column(db.Float, nullable=False)
    amount_received = db.Column(db.Float, default=0.0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Added this line

    donations = db.relationship("Donation", secondary=donation_case, back_populates="cases")