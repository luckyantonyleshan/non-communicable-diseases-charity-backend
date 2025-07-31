from app import create_app
from app.extensions import db
from app.models import User, Case, Disease, Area, Donation, Resource, Review
import os

def seed_database():
    app = create_app()
    
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()

        # Create admin user with strong password
        admin = User(
            username='admin',
            email='admin@example.com',
            role='admin'
        )
        admin.set_password(os.getenv('ADMIN_PASSWORD', 'SecureAdminPass123!'))
        db.session.add(admin)

        # Create test user
        test_user = User(
            username='testuser',
            email='user@example.com',
            role='user'
        )
        test_user.set_password('TestUserPass123!')
        db.session.add(test_user)

        db.session.commit()

        # Create sample disease
        diabetes = Disease(
            name='Diabetes',
            description='Chronic metabolic disorder',
            prevalence=9.3
        )
        db.session.add(diabetes)

        # Create sample case
        case = Case(
            title='Diabetes Awareness',
            description='Education and prevention program',
            amount_needed=10000,
            amount_received=0,
            user_id=admin.id
        )
        db.session.add(case)

        db.session.commit()

        print("""
        Database seeded successfully!
        Admin credentials:
        - Username: admin
        - Password: SecureAdminPass123! (or check your ADMIN_PASSWORD env var)
        
        Test user credentials:
        - Username: testuser
        - Password: TestUserPass123!
        """)

if __name__ == '__main__':
    seed_database()