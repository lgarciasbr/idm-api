from idManager.model.database.db_model import db, Account
from idManager.model import message_service


def register_account(email, password):
    try:
        db.session.add(Account(email, password))
        db.session.commit()

        return True
    except Exception as e:
        message_service.exception('register_account', repr(e))
        return False


def get_account_by_email(email):
    try:
        return Account.query.filter_by(email=email).first()
    except Exception as e:
        message_service.exception('get_account_by_email', repr(e))
        return None


def get_account_by_id(pk):
    try:
        return Account.query.get(pk)
    except Exception as e:
        message_service.exception('get_account_by_id', repr(e))
        return None


def get_accounts(page, per_page):
    try:
        return Account.query.paginate(page, per_page, error_out=False)
    except Exception as e:
        message_service.exception('get_accounts', repr(e))
        return None


def change_account_password(pk, new_password):
    try:
        account = Account.query.get(pk)
        account.password = new_password
        db.session.commit()

        return True
    except Exception as e:
        message_service.exception('change_account_password', repr(e))
        return False


def delete_account_by_id(pk):
    try:
        Account.query.filter_by(id=pk).delete()
        db.session.commit()

        return True
    except Exception as e:
        message_service.exception('delete_account_by_id', repr(e))
        return False
