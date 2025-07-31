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
        # Drop all tables
        db.drop_all()
        print("Dropped all tables")
        
        # Create all tables
        db.create_all()
        print("Created all tables")

        # Seed admin user
        admin = User(username='admin', email='admin@example.com', role='admin')
        admin.set_password('password123')
        db.session.add(admin)

        # Seed test user
        user = User(username='testuser', email='test@example.com', role='user')
        user.set_password('password123')
        db.session.add(user)

        # Commit users to assign IDs
        db.session.commit()
        print("Users committed: admin and testuser")

        # Seed cases
        case = Case(
            title='Diabetes Awareness',
            description='Educate about diabetes prevention',
            amount_needed=5000.00,
            amount_received=0.00,
            user_id=admin.id
        )
        db.session.add(case)

        # Seed diseases
        disease = Disease(
            name='Diabetes',
            description='A chronic condition affecting blood sugar levels',
            prevalence=9.3
        )
        db.session.add(disease)

        # Seed areas
        areas = [
            Area(
                name='Nairobi, Kenya',
                description='High prevalence of diabetes in urban areas',
                latitude=-1.286389,
                longitude=36.817223
            ),
            Area(
                name='Kinshasa, DRC',
                description='Major urban center',
                latitude=-4.441931,
                longitude=15.266293
            ),
            Area(
                name='Dhaka, Bangladesh',
                description='Densely populated city',
                latitude=23.810332,
                longitude=90.412518
            ),
            Area(
                name='Lagos, Nigeria',
                description='Economic hub',
                latitude=6.524379,
                longitude=3.379206
            ),
            Area(
                name='Karachi, Pakistan',
                description='Coastal city',
                latitude=24.860734,
                longitude=67.001136
            ),
            Area(
                name='Mumbai, India',
                description='Financial capital',
                latitude=19.075984,
                longitude=72.877656
            ),
        ]
        db.session.add_all(areas)

        # Commit case, disease, and areas to assign IDs
        db.session.commit()
        print("Case, disease, and areas committed")

        # Seed donation
        donation = Donation(
            amount=100.00,
            donor_name='John Doe',
            user_id=admin.id,
            case_id=case.id,
            area_id=areas[0].id
        )
        db.session.add(donation)

        # Seed resource
        resource = Resource(
            title='Diabetes Guide',
            url='https://example.com/diabetes-guide'
        )
        db.session.add(resource)

        # Seed review
        review = Review(
            content='We need more awareness campaigns in Nairobi!',
            user_id=admin.id,
            disease_id=disease.id,
            area_id=areas[0].id
        )
        db.session.add(review)

        # Final commit
        db.session.commit()
        print('Database seeded successfully with admin (username: admin, password: password123) and test user (username: testuser, password: password123)!')

if __name__ == '__main__':
    seed_database()