from app import create_app
from app.extensions import db
from app.models.user import User
from app.models.case import Case
from app.models.donation import Donation
from app.models.resource import Resource
from app.models.disease import Disease
from app.models.area import Area
from app.models.review import Review
from datetime import datetime

def seed_database():
    app = create_app()
    
    with app.app_context():
        print("\n=== Starting Database Seeding ===")
        
        try:
            # Drop all tables (keeps your existing reset logic)
            db.drop_all()
            print("✔ Dropped all tables")
            
            # Create all tables
            db.create_all()
            print("✔ Created all tables")

            # ===== User Seeding =====
            # Admin user with verification
            admin = User(
                username='admin',
                email='admin@example.com',
                role='admin',
                created_at=datetime.utcnow()
            )
            admin.set_password('password123')
            db.session.add(admin)

            # Test user
            user = User(
                username='testuser',
                email='test@example.com',
                role='user',
                created_at=datetime.utcnow()
            )
            user.set_password('password123')
            db.session.add(user)

            db.session.commit()
            print(f"✔ Users created - Admin ID: {admin.id}, User ID: {user.id}")

            # ===== Disease Seeding =====
            diseases = [
                Disease(
                    name='Diabetes',
                    description='A chronic condition affecting blood sugar levels',
                    prevalence=9.3
                ),
                Disease(
                    name='Hypertension',
                    description='High blood pressure condition',
                    prevalence=15.2
                ),
                Disease(
                    name='Heart Disease',
                    description='Various conditions affecting the heart',
                    prevalence=6.7
                )
            ]
            db.session.add_all(diseases)
            db.session.commit()
            print(f"✔ Created {len(diseases)} diseases")

            # ===== Area Seeding =====
            areas = [
                Area(
                    name='Nairobi, Kenya',
                    description='High prevalence of diabetes in urban areas',
                    latitude=-1.286389,
                    longitude=36.817223
                ),
                Area(
                    name='Kinshasa, DRC',
                    description='Major urban center with health challenges',
                    latitude=-4.441931,
                    longitude=15.266293
                ),
                Area(
                    name='Dhaka, Bangladesh',
                    description='Densely populated city with health concerns',
                    latitude=23.810332,
                    longitude=90.412518
                ),
                Area(
                    name='Lagos, Nigeria',
                    description='Economic hub with growing health needs',
                    latitude=6.524379,
                    longitude=3.379206
                ),
                Area(
                    name='Mumbai, India',
                    description='Financial capital with health disparities',
                    latitude=19.075984,
                    longitude=72.877656
                )
            ]
            db.session.add_all(areas)
            db.session.commit()
            print(f"✔ Created {len(areas)} geographic areas")

            # ===== Case Seeding =====
            cases = [
                Case(
                    title='Diabetes Awareness Campaign',
                    description='Educate communities about diabetes prevention',
                    amount_needed=5000.00,
                    amount_received=1200.00,
                    user_id=admin.id
                ),
                Case(
                    title='Heart Health Initiative',
                    description='Promote heart-healthy lifestyle choices',
                    amount_needed=3000.00,
                    amount_received=800.00,
                    user_id=user.id
                ),
                Case(
                    title='Hypertension Screening Program',
                    description='Free blood pressure screening',
                    amount_needed=2500.00,
                    amount_received=500.00,
                    user_id=admin.id
                )
            ]
            db.session.add_all(cases)
            db.session.commit()
            print(f"✔ Created {len(cases)} cases")

            # ===== Resource Seeding =====
            resources = [
                Resource(
                    title='Diabetes Prevention Guide',
                    url='https://example.com/diabetes-guide'
                ),
                Resource(
                    title='Heart Health Tips',
                    url='https://example.com/heart-health'
                ),
                Resource(
                    title='Managing Hypertension',
                    url='https://example.com/hypertension-management'
                )
            ]
            db.session.add_all(resources)
            db.session.commit()
            print(f"✔ Created {len(resources)} resources")

            # ===== Donation Seeding =====
            donations = [
                Donation(
                    amount=500.00,
                    donor_name='John Doe',
                    user_id=admin.id,
                    case_id=cases[0].id,
                    area_id=areas[0].id
                ),
                Donation(
                    amount=300.00,
                    donor_name='Jane Smith',
                    user_id=user.id,
                    case_id=cases[1].id,
                    area_id=areas[1].id
                ),
                Donation(
                    amount=200.00,
                    donor_name='Anonymous',
                    user_id=admin.id,
                    case_id=cases[2].id,
                    area_id=areas[2].id
                )
            ]
            db.session.add_all(donations)
            db.session.commit()
            print(f"✔ Created {len(donations)} donations")

            # ===== Review Seeding =====
            reviews = [
                Review(
                    content='We need more diabetes awareness programs in Nairobi.',
                    user_id=admin.id,
                    disease_id=diseases[0].id,
                    area_id=areas[0].id
                ),
                Review(
                    content='Heart disease is a major concern in our community.',
                    user_id=user.id,
                    disease_id=diseases[2].id,
                    area_id=areas[3].id
                ),
                Review(
                    content='Hypertension rates in urban areas are alarming.',
                    user_id=admin.id,
                    disease_id=diseases[1].id,
                    area_id=areas[4].id
                )
            ]
            db.session.add_all(reviews)
            db.session.commit()
            print(f"✔ Created {len(reviews)} reviews")

            # ===== Final Output =====
            print("\n⭐ Database seeded successfully! ⭐")
            print("=== Login Credentials ===")
            print("Admin: username='admin' | password='password123'")
            print("User:  username='testuser' | password='password123'")
            print("=========================\n")
            
        except Exception as e:
            db.session.rollback()
            print(f"\n❌ Seeding failed: {str(e)}\n")
            raise

if __name__ == '__main__':
    seed_database()