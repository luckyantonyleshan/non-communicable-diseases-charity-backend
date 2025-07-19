from app.extensions import db
from app.models.user import User
from app.models.case import Case
from app.models.donation import Donation
from app.models.resource import Resource
from app import create_app

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    u1 = User(username="admin", email="admin@example.com")
    u1.set_password("password")
    db.session.add(u1)

    c1 = Case(title="Diabetes Awareness", description="Educating people about Type 2 Diabetes.")
    db.session.add(c1)

    d1 = Donation(amount=1000, donor_name="John Doe")
    db.session.add(d1)

    r1 = Resource(title="Diabetes Guide", url="https://example.com/diabetes-guide")
    db.session.add(r1)

    db.session.commit()
