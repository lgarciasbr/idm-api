from idManager.model.database.db_model import db, db_redis, Token
from idManager.settings import TOKEN_HOST
from idManager.model import message_service
import datetime


def set_token(account, token):
    try:
        if TOKEN_HOST == 'redis':
            db_redis.hset(account.id, token, datetime.datetime.now())

            return True
        elif TOKEN_HOST == 'database':
            db.session.add(Token(account, token))
            db.session.commit()

            return True
        else:
            return False
    except Exception as e:
        message_service.exception('set_token', repr(e))
        return False


def get_token_last_accessed_date(account_id, token):
    try:
        if TOKEN_HOST == 'redis':
            last_accessed_date = (db_redis.hget(account_id, token)).decode('ascii')
            return datetime.datetime.strptime(last_accessed_date, "%Y-%m-%d %H:%M:%S.%f")
        elif TOKEN_HOST == 'database':
            token = Token.query.filter_by(token=token, account_id=account_id).first()
            return token.last_accessed_date
        else:
            return None
    except Exception as e:
        message_service.exception('get_token_last_accessed_date', repr(e))
        return None


def change_last_accessed_date(account_id, token):
    try:
        if TOKEN_HOST == 'redis':
            db_redis.hset(account_id, token, datetime.datetime.now())

            return True
        elif TOKEN_HOST == 'database':
            token = Token.query.filter_by(token=token).first()
            token.last_accessed_date = datetime.datetime.now()
            db.session.commit()

            return True
        else:
            return False
    except Exception as e:
        message_service.exception('change_last_accessed_date', repr(e))
        return False


def delete_token(account_id, token):
    try:
        if TOKEN_HOST == 'redis':
            db_redis.hdel(account_id, token)

            return True
        elif TOKEN_HOST == 'database':
            Token.query.filter_by(token=token).delete()
            db.session.commit()

            return True
        else:
            return False
    except Exception as e:
        message_service.exception('delete_token', repr(e))
        return False


def delete_token_by_account_id(pk):
    try:
        if TOKEN_HOST == 'redis':
            db_redis.delete(pk)

            return True
        elif TOKEN_HOST == 'database':
            Token.query.filter_by(account_id=pk).delete()
            db.session.commit()

            return True
        else:
            return False
    except Exception as e:
        message_service.exception('delete_token_by_account_id', repr(e))
        return False
