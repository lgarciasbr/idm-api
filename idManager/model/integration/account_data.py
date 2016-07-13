from idManager.model.database.db_model import db, Account, AccountSchema

account_schema_post = AccountSchema(only=('email', 'password'))
account_schema_put = AccountSchema(only=('password', 'new_password'))
account_schema_get = AccountSchema(only=('email', 'url', 'created_at', 'id'))
accounts_schema_get = AccountSchema(many=True, only=('email', 'url', 'id'))


def register_account(email, password):
    try:
        db.session.add(Account(email, password))
        db.session.commit()

        return True
    except:
        return False


def get_account(email):
    try:
        account = Account.query.filter_by(email=email).first()
    except:
        return None
    return account


def get_account_by_email(email):
    try:
        account = Account.query.filter_by(email=email).first()

        # Serialize the queryset
        return account_schema_get.dump(account)
    except:
        return None


def get_account_by_id(pk):
    try:
        account = Account.query.get(pk)

        # Serialize the queryset
        return account_schema_get.dump(account)
    except:
        return None


def get_accounts():
    try:
        accounts = Account.query.all()

        # Serialize the queryset
        return accounts_schema_get.dump(accounts)
    except:
        return None


def delete_account(pk):
    try:
        # todo apagar todas as sessões antes.
        Account.query.filter_by(id=pk).delete()
        db.session.commit()

        return True
    except:
        return False


# todo unittest
# todo melhorar o uso do try expect
# todo deixar estas duas func genericas: by_email e by_id
