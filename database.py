from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.orm import backref
from marshmallow import Schema, fields, ValidationError, pre_load

db = SQLAlchemy()


# TODO Precisa testar para verificar se o sistema esta diferenciando maiuscula de minuscula.
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.Binary, unique=False)
    created_at = db.Column(db.DateTime, nullable=False, default=func.now())

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return self.email

    @property
    def url(self):
        return url_for('accounts.accounts_get', id=self.id, _external=True)


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


# region Schema

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    email = fields.Email()
    url = fields.Url(dump_only=True)

# endregion
