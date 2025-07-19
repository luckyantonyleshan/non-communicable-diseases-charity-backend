from app.extensions import db

donation_case = db.Table('donation_case',
    db.Column('donation_id', db.Integer, db.ForeignKey('donation.id')),
    db.Column('case_id', db.Integer, db.ForeignKey('case.id'))
)
