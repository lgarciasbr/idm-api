from database import db, User


def register(email, password):
    db.session.add(User(email, password))
    db.session.commit()
