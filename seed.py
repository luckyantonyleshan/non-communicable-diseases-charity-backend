import app.extensions
import app.models.user
import app.models.case
import app.models.donation
import app.models.resource
import app
from werkzeug.security import generate_password_hash

app_instance = app.create_app()

with app_instance.app_context():
    app.extensions.db.drop_all()
    app.extensions.db.create_all()

    if not app.models.user.User.query.first():
        user = app.models.user.User(username="admin", email="admin@example.com")
        user.set_password("password")
        app.extensions.db.session.add(user)
        app.extensions.db.session.commit()
        print("Seeded default user.")
    else:
        print("Users already exist.")

    u1 = app.models.user.User(username="user1", email="user1@example.com")
    u1.set_password("password123")
    app.extensions.db.session.add(u1)

    c1 = app.models.case.Case(title="Diabetes Awareness", description="Educating people about Type 2 Diabetes", user_id=1)
    app.extensions.db.session.add(c1)

    d1 = app.models.donation.Donation(amount=1000, donor_name="John Doe", user_id=1)
    app.extensions.db.session.add(d1)

    r1 = app.models.resource.Resource(title="Diabetes Guide", url="https://example.com/diabetes-guide")
    app.extensions.db.session.add(r1)

    app.extensions.db.session.commit()
    print("Seeded initial data.")