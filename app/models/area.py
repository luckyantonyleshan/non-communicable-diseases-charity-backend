from app.extensions import db

class Area(db.Model):
    __tablename__ = 'areas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    latitude = db.Column(db.Float, nullable=True)  # For map integration
    longitude = db.Column(db.Float, nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    diseases = db.relationship('Disease', secondary='disease_area', back_populates='areas')
    reviews = db.relationship('Review', back_populates='area')
    donations = db.relationship('Donation', back_populates='area')