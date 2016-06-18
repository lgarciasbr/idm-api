from database import db, User, UserSchema


def register(email, password):
    db.session.add(User(email, password))
    db.session.commit()


def get_first(email):
    return User.query.filter_by(email=email).first()


user_schema = UserSchema()
users_schema = UserSchema(many=True)


# todo http://marshmallow.readthedocs.io/en/latest/examples.html
def get():
    users = User.query.all()
    # Serialize the queryset
    return users_schema.dump(users)

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