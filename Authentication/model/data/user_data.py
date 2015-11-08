from database import User


def get_user(email):
    return User.query.filter_by(email=email).first()
