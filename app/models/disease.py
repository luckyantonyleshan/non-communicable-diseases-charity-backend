from app.extensions import db

class Disease(db.Model):
    __tablename__ = 'diseases'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    prevalence = db.Column(db.Float, nullable=False, default=0.0)  
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    areas = db.relationship('Area', secondary='disease_area', back_populates='diseases')
    reviews = db.relationship('Review', back_populates='disease')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'prevalence': self.prevalence,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }