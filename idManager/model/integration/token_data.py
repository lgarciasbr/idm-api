from idManager.model.database.db_model import db, Token


def set_token(token, account):
    try:
        db.session.add(Token(token, account))
        db.session.commit()

        return True

    except:
        return False


def get_token(token):
    try:
        return Token.query.filter_by(token=token).first()

    except:
        return None


def delete_token(token):
    try:
        Token.query.filter_by(token=token).delete()
        db.session.commit()

        return True
    except:
        return False


def delete_token_by_account_id(pk):
    try:
        Token.query.filter_by(account_id=pk).delete()
        db.session.commit()

        return True
    except:
        return False


# todo melhorar o uso do try expect
