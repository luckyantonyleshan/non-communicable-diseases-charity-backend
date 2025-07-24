from app.extensions import db
from app.models.association import donation_case

class Donation(db.Model):
    __tablename__ = 'donations'

    id = db.Column(db.Integer, primary_key=True)
    donor_name = db.Column(db.String(120), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    case_id = db.Column(db.Integer, db.ForeignKey('cases.id'), nullable=True)
    area_id = db.Column(db.Integer, db.ForeignKey('areas.id'), nullable=True)

    user = db.relationship('User', back_populates='donations')
    cases = db.relationship('Case', secondary=donation_case, back_populates='donations')
    area = db.relationship('Area', back_populates='donations')

    def to_dict(self):
        return {
            'id': self.id,
            'amount': self.amount,
            'donor_name': self.donor_name,
            'user_id': self.user_id,
            'case_id': self.case_id,
            'area_id': self.area_id
        }