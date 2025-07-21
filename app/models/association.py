from app.extensions import db

donation_case = db.Table(
    'donation_case',
    db.Column('donation_id', db.Integer, db.ForeignKey('donations.id'), primary_key=True),
    db.Column('case_id', db.Integer, db.ForeignKey('cases.id'), primary_key=True)
)
