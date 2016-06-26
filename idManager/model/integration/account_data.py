from idManager.model.database.db_model import db, Account, AccountSchema

account_schema_post = AccountSchema(only=('email', 'password'))
account_schema_put = AccountSchema(only=('password', 'new_password'))
account_schema_get = AccountSchema(only=('email', 'url', 'created_at', 'id'))
accounts_schema_get = AccountSchema(many=True, only=('email', 'url'))

# todo unittest
# todo melhorar o uso do try expect


def register_account(email, password):
    try:
        db.session.add(Account(email, password))
        db.session.commit()

        account = Account.query.filter_by(email=email).first()

        return account_schema_get.dump(account)
    except:
        return None


def get_account(email):
    try:
        account = Account.query.filter_by(email=email).first()
    except:
        return None
    return account


# todo deixar estas duas func genericas: by_email e by_id
def get_account_by_email(email):
    try:
        account = Account.query.filter_by(email=email).first()
    except:
        return None
    return account_schema_get.dump(account)


def get_account_by_id(pk):
    try:
        account = Account.query.get(pk)
    except:
        return None
    # Serialize the queryset
    return account_schema_get.dump(account)


def get_accounts():
    try:
        accounts = Account.query.all()
    except:
        return None
    # Serialize the queryset
    return accounts_schema_get.dump(accounts)


def delete_account(pk):
    try:
        # todo apagar todas as sessões antes.
        Account.query.filter_by(id=pk).delete()
        db.session.commit()
        return True
    except:
        return False

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