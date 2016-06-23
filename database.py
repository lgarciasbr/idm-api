from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.orm import backref
from marshmallow import Schema, fields, ValidationError, pre_load

db = SQLAlchemy()


# TODO Precisa testar para verificar se o sistema esta diferenciando maiuscula de minuscula.
class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.Binary, unique=False, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=func.now())

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return self.email

    @property
    def url(self):
        return url_for('accounts.account_get', pk=self.id, _external=True)


class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(200), unique=False)
    account_id = db.Column(db.Integer, db.ForeignKey(Account.id), nullable=False)
    account = db.relationship(Account, backref=backref('tokens'))

    def __init__(self, token, account):
        self.token = token
        self.account = account

    def __repr__(self):
        return self.token


# region Schema

# Custom validator
def must_not_be_blank(data):
    if not data:
        raise ValidationError('Data not provided.')


class AccountSchema(Schema):
    id = fields.Int(dump_only=True)
    password = fields.String(required=True, validate=must_not_be_blank)
    # new_password is used at change_password api method
    new_password = fields.String(required=True, validate=must_not_be_blank)
    email = fields.Email(required=True)
    url = fields.Url(dump_only=True)
    created_at = fields.DateTime(dump_only=True)

# endregion
