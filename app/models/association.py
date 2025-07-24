from app.extensions import db

donation_case = db.Table(
    'donation_case',
    db.Column('donation_id', db.Integer, db.ForeignKey('donations.id'), primary_key=True),
    db.Column('case_id', db.Integer, db.ForeignKey('cases.id'), primary_key=True)
)

disease_area = db.Table(
    'disease_area',
    db.Column('disease_id', db.Integer, db.ForeignKey('diseases.id'), primary_key=True),
    db.Column('area_id', db.Integer, db.ForeignKey('areas.id'), primary_key=True)
)