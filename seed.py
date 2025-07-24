from app import create_app
from app.extensions import db
from app.models.user import User
from app.models.case import Case
from app.models.donation import Donation
from app.models.resource import Resource
from app.models.disease import Disease
from app.models.area import Area
from app.models.review import Review

def seed_database():
    app = create_app()
    
    with app.app_context():
        if not User.query.first():
            user = User(username='admin', email='admin@example.com', role='admin')
            user.set_password('password123')
            db.session.add(user)

            case = Case(
                title='Diabetes Awareness',
                description='Educate about diabetes prevention',
                amount_needed=5000.00,
                amount_received=0.00,
                user_id=user.id
            )
            db.session.add(case)

            disease = Disease(
                name='Diabetes',
                description='A chronic condition affecting blood sugar levels',
                prevalence=9.3
            )
            db.session.add(disease)

            area = Area(
                name='Nairobi',
                description='High prevalence of diabetes in urban areas',
                latitude=-1.286389,
                longitude=36.817223
            )
            db.session.add(area)

            donation = Donation(
                amount=100.00,
                donor_name='John Doe',
                user_id=user.id,
                case_id=case.id,
                area_id=area.id
            )
            db.session.add(donation)

            resource = Resource(
                title='Diabetes Guide',
                url='https://example.com/diabetes-guide'
            )
            db.session.add(resource)

            review = Review(
                content='We need more awareness campaigns in Nairobi!',
                user_id=user.id,
                disease_id=disease.id,
                area_id=area.id
            )
            db.session.add(review)

            db.session.commit()
            print('Database seeded successfully!')
        else:
            print('Database already contains data - skipping seed')

if __name__ == '__main__':
    seed_database()