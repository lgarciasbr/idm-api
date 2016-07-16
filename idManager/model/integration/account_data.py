from idManager.model.database.db_model import db, Account


def register_account(email, password):
    try:
        db.session.add(Account(email, password))
        db.session.commit()

        return True
    except:
        return False


def get_account_by_email(email):
    try:
        return Account.query.filter_by(email=email).first()
    except:
        return None


def get_account_by_id(pk):
    try:
        return Account.query.get(pk)
    except:
        return None


def get_accounts():
    try:
        return Account.query.all()
    except:
        return None


# todo apagar todas as sessões antes.
def delete_account_by_id(pk):
    try:
        Account.query.filter_by(id=pk).delete()
        db.session.commit()

        return True
    except:
        return False

# todo melhorar o uso do try expect
# todo deixar estas duas func genericas: by_email e by_id
