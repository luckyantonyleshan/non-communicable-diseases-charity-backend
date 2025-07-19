from flask_jwt_extended import get_jwt_identity
import app.models.user

def get_current_user():
    user_id = get_jwt_identity()
    return app.models.user.User.query.get(user_id)