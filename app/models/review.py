from app.extensions import db

class Review(db.Model):
    __tablename__ = 'reviews'
    __table_args__ = (
        db.Index('ix_reviews_user_id', 'user_id'),
        db.Index('ix_reviews_disease_id', 'disease_id'),
        db.Index('ix_reviews_area_id', 'area_id'),
    )

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
            'username': self.user.username if self.user else 'Anonymous',
            'disease_id': self.disease_id,
            'disease_name': self.disease.name if self.disease else None,
            'area_id': self.area_id,
            'area_name': self.area.name if self.area else 'Unknown Area',
            'created_at': self.created_at.isoformat() if self.created_at else None
        }