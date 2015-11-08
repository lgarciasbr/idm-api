from database import db, User


def register(email, password):
    db.session.add(User(email, password))
    db.session.commit()

# TODO o mesmo arquivo no modulo authentication tem este mesmo codigo.
def get_user(email):
    return User.query.filter_by(email=email).first()
