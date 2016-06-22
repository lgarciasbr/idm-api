from database import db, Account, AccountSchema

account_schema_post = AccountSchema(only=('email', 'password'))
account_schema = AccountSchema(only=('email', 'url', 'created_at', 'id'))
accounts_schema = AccountSchema(many=True, only=('email', 'url'))


def register(email, password):
    db.session.add(Account(email, password))
    db.session.commit()


def get_first(email):
    try:
        account = Account.query.filter_by(email=email).first()
    except:
        return None
    return account


# todo unittest
def accounts_get():
    try:
        account = Account.query.all()
    except:
        return None
    # Serialize the queryset
    return accounts_schema.dump(account)


def account_get(pk):
    try:
        account = Account.query.get(pk)
    except:
        return None
    # Serialize the queryset
    return account_schema.dump(account)

# todo trocar de 'data' para 'integration'

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