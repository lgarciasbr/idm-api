import bmemcached
from idManager.model.database.db_model import db, Token, TokenSchema
from idManager.settings import TOKEN_HOST, MEMCACHED_URL, MEMCACHED_USERNAME, MEMCACHED_PASSWORD

client = bmemcached.Client(MEMCACHED_URL, MEMCACHED_USERNAME, MEMCACHED_PASSWORD)
token_schema_get = TokenSchema()


def set_token(token, account):
    if TOKEN_HOST == 'memcached':
        client.set(token, account.id)
        return token
    elif TOKEN_HOST == 'database':
        try:
            db.session.add(Token(token, account))
            db.session.commit()

            registered_token = Token.query.filter_by(token=token).first()

            return token_schema_get.dump(registered_token)
        except:
            return None
    else:
        return None


def get_token(token):
    if TOKEN_HOST == 'memcached':
        account_id_registered_token = client.get(token)
        return account_id_registered_token
    elif TOKEN_HOST == 'database':
        registered_token = Token.query.filter_by(token=token).first()

        if registered_token is not None:
            return registered_token.account_id
        else:
            return None
    else:
        return None


def delete_token(token):
    if TOKEN_HOST == 'memcached':
        return client.delete(token)
    elif TOKEN_HOST == 'database':
        Token.query.filter_by(token=token).delete()
        db.session.commit()
    else:
        return None


# todo criar os unittests do memcached
# todo melhorar o retorno de erro quando o memcahed esta fora do ar, so da problema com o logout.
