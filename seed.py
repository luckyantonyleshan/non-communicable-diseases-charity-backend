from app import create_app
from app.extensions import db
from app.models.user import User
from app.models.case import Case
from app.models.donation import Donation
from app.models.resource import Resource

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    user = User(
        username="admin",
        email="admin@example.com"
    )
    user.set_password("password123")
    db.session.add(user)
    db.session.commit()

    case = Case(
        title="Diabetes Awareness",
        description="Educate about diabetes prevention",
        amount_needed=5000.00,
        amount_received=0.00,
        user_id=user.id
    )
    db.session.add(case)
    db.session.commit()

    donation = Donation(
        amount=100.00,
        donor_name="John Doe",
        user_id=user.id,
        case_id=case.id  
    )
    db.session.add(donation)
    db.session.commit()

    resource = Resource(
        title="Diabetes Guide",
        url="https://example.com/diabetes-guide"
    )
    db.session.add(resource)
    db.session.commit()

    print("Database seeded successfully!")