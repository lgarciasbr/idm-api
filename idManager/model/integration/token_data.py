from idManager.model.database.db_model import db, Token
from flask import current_app
import datetime
import redis


# db_redis = redis.Redis('192.168.99.100', '32769')
# db_redis.set('test_key', 'test_value')
# value = db_redis.get('test_key')
# token_redis = {"token": '123', "id": '1'}
# db_redis.hmset('token_session', token_redis)
# value = db_redis.hget('token_session', '123')


def set_token(account, token):
    try:
        db.session.add(Token(account, token))
        db.session.commit()

        return True

    except:
        current_app.extensions['sentry'].captureException()
        return False


def get_token(token):
    try:
        return Token.query.filter_by(token=token).first()

    except:
        current_app.extensions['sentry'].captureException()
        return None


def change_last_accessed_date(token):
    try:
        token = Token.query.filter_by(token=token).first()
        token.last_accessed_date = datetime.datetime.now()
        db.session.commit()

        return True
    except:
        current_app.extensions['sentry'].captureException()
        return False


def delete_token(token):
    try:
        Token.query.filter_by(token=token).delete()
        db.session.commit()

        return True
    except:
        current_app.extensions['sentry'].captureException()
        return False


def delete_token_by_account_id(pk):
    try:
        Token.query.filter_by(account_id=pk).delete()
        db.session.commit()

        return True
    except:
        current_app.extensions['sentry'].captureException()
        return False
