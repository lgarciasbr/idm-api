import bmemcached
from database import db, Token
from settings import TOKEN_HOST, MEMCACHED_URL, MEMCACHED_USERNAME, MEMCACHED_PASSWORD

client = bmemcached.Client(MEMCACHED_URL, MEMCACHED_USERNAME, MEMCACHED_PASSWORD)


#todo criar os unittests do memcached
def get_token(token):
    if TOKEN_HOST == 'memcached':
        user_id_registered_token = client.get(token)
        return user_id_registered_token
    elif TOKEN_HOST == 'database':
        registered_token = Token.query.filter_by(token=token).first()

        if registered_token is not None:
            return registered_token.user_id
        else:
            return None
    else:
        pass


def set_token(token, user):
    if TOKEN_HOST == 'memcached':
        bla = client.set(token, user.id)
        return token
    elif TOKEN_HOST == 'database':
        db.session.add(Token(token, user))
        db.session.commit()
        return token


def delete_token(token):
    if TOKEN_HOST == 'memcached':
        return client.delete(token)
    elif TOKEN_HOST == 'database':
        Token.query.filter_by(token=token).delete()
        db.session.commit()


'''
class MyAdapter(DBAdapter):

    def get_object(self, ObjectClass, id):
        """ Retrieve one object specified by the primary key 'pk' """
        pass

    def find_all_objects(self, ObjectClass, **kwargs):
         """ Retrieve all objects matching the case sensitive filters in 'kwargs'. """
        pass


    def find_first_object(self, ObjectClass, **kwargs):
        """ Retrieve the first object matching the case sensitive filters in 'kwargs'. """
        pass

    def ifind_first_object(self, ObjectClass, **kwargs):
        """ Retrieve the first object matching the case insensitive filters in 'kwargs'. """
        pass

    def add_object(self, ObjectClass, **kwargs):
        """ Add an object of class 'ObjectClass' with fields and values specified in '**kwargs'. """
        pass

    def update_object(self, object, **kwargs):
        """ Update object 'object' with the fields and values specified in '**kwargs'. """
        pass

    def delete_object(self, object):
        """ Delete object 'object'. """
        pass

    def commit(self):
        pass
'''
