from idManager.model.database.db_model import db, Account
from flask import current_app


def register_account(email, password):
    try:
        db.session.add(Account(email, password))
        db.session.commit()

        return True
    except:
        current_app.extensions['sentry'].captureException()
        return False


def get_account_by_email(email):
    try:
        return Account.query.filter_by(email=email).first()
    except:
        current_app.extensions['sentry'].captureException()
        return None


def get_account_by_id(pk):
    try:
        return Account.query.get(pk)
    except:
        current_app.extensions['sentry'].captureException()
        return None


def get_accounts():
    try:
        return Account.query.all()
    except:
        current_app.extensions['sentry'].captureException()
        return None


def change_account_password(pk, new_password):
    try:
        account = Account.query.get(pk)
        account.password = new_password
        db.session.commit()

        return True
    except:
        current_app.extensions['sentry'].captureException()
        return False


def delete_account_by_id(pk):
    try:
        Account.query.filter_by(id=pk).delete()
        db.session.commit()

        return True
    except:
        current_app.extensions['sentry'].captureException()
        return False
