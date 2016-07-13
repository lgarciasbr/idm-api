import bmemcached
from idManager.model.database.db_model import db, Token
from idManager.settings import TOKEN_HOST, MEMCACHED_URL, MEMCACHED_USERNAME, MEMCACHED_PASSWORD

client = bmemcached.Client(MEMCACHED_URL, MEMCACHED_USERNAME, MEMCACHED_PASSWORD)


def set_token(token, account):
    if TOKEN_HOST == 'memcached':
        client.set(token, account.id)
        return token
    elif TOKEN_HOST == 'database':
        try:
            db.session.add(Token(token, account))
            db.session.commit()

            return True
        except:
            return False
    else:
        return None


def get_token(token):
    if TOKEN_HOST == 'memcached':
        account_id_registered_token = client.get(token)
        return account_id_registered_token
    elif TOKEN_HOST == 'database':
        try:
            return Token.query.filter_by(token=token).first()
        except:
            return None

    else:
        return None


def delete_token(token):
    if TOKEN_HOST == 'memcached':
        return client.delete(token)
    elif TOKEN_HOST == 'database':
        Token.query.filter_by(token=token).delete()
        db.session.commit()

        return True
    else:
        return False


# todo criar os unittests do memcached
# todo melhorar o retorno de erro quando o memcahed esta fora do ar, so da problema com o logout.
