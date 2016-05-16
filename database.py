from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.orm import backref

db = SQLAlchemy()


# TODO Precisa testar para verificar se o sistema esta diferenciando maiuscula de minuscula.
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(80), unique=False)
    created_at = db.Column(db.DateTime, nullable=False, default=func.now())

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return self.email


class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(200), unique=False)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    user = db.relationship(User, backref=backref('tokens'))

    def __init__(self, token, user):
        self.token = token
        self.user = user

    def __repr__(self):
        return self.token
