from app.extensions import db

class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    disease_id = db.Column(db.Integer, db.ForeignKey('diseases.id'), nullable=True)
    area_id = db.Column(db.Integer, db.ForeignKey('areas.id'), nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    user = db.relationship('User', back_populates='reviews')
    disease = db.relationship('Disease', back_populates='reviews')
    area = db.relationship('Area', back_populates='reviews')

    def to_dict(self):
        return {
            'id': self.id,
            'content': self.content,
            'user_id': self.user_id,
            'disease_id': self.disease_id,
            'area_id': self.area_id,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
