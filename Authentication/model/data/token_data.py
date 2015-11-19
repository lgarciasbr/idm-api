from pymemcache.client import Client
from database import db, Token

from lib.json import json_serializer, json_deserializer
from config import MEMCACHED_HOST, MEMCACHED_PORT, TOKEN_HOST

client = Client((MEMCACHED_HOST, MEMCACHED_PORT), serializer=json_serializer, deserializer=json_deserializer)


#todo criar os unittests do memcached
def get_token(email):
    if TOKEN_HOST == 'memcached':
        return client.get(email)
    elif TOKEN_HOST == 'database':
        return Token.query.filter_by(token=email).first()
    else:
        pass


def set_token(token, value):
    if TOKEN_HOST == 'memcached':
        client.set(token, value)
        return token
    elif TOKEN_HOST == 'database':
        db.session.add(Token(token, value['email']))
        db.session.commit()
        return token


def delete_token(token):
    if TOKEN_HOST == 'memcached':
        return client.delete(token)
    elif TOKEN_HOST == 'database':
        pass
        #todo criar o codigo para apagar o token via base de dados


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
