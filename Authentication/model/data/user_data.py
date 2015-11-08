from database import User

# TODO o mesmo arquivo no modulo account tem este mesmo codigo.
def get_user(email):
    return User.query.filter_by(email=email).first()
