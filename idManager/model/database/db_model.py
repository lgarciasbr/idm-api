from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.orm import backref
from idManager.settings import TOKEN_HOST, REDIS_URL
import redis

db = SQLAlchemy()

if TOKEN_HOST == 'redis':
    db_redis = redis.from_url(REDIS_URL)
else:
    db_redis = ''


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=func.now())

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    @property
    def url(self):
        return url_for('api.get_group_by_id', pk=self.id, _external=True)


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
        return url_for('api.get_account_by_id', pk=self.id, _external=True)


class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey(Account.id), unique=False, nullable=False)
    token = db.Column(db.String(200), unique=False, nullable=False)
    last_accessed_date = db.Column(db.DateTime, nullable=False, default=func.now())
    account = db.relationship(Account, backref=backref('tokens'))

    def __init__(self, account, token):
        self.account = account
        self.token = token

    def __repr__(self):
        return self.token
