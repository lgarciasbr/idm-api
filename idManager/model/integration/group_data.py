from idManager.model.database.db_model import db, Group
from idManager.model import message_service


def register_group(name):
    try:
        db.session.add(Group(name))
        db.session.commit()

        return True
    except Exception as e:
        message_service.exception('register_group', repr(e))
        return False


def get_group_by_name(name):
    try:
        return Group.query.filter_by(name=name).first()
    except Exception as e:
        message_service.exception('get_group_by_name', repr(e))
        return None


def get_group_by_id(pk):
    try:
        return Group.query.get(pk)
    except Exception as e:
        message_service.exception('get_group_by_id', repr(e))
        return None


def get_groups(page, per_page):
    try:
        return Group.query.paginate(page, per_page, error_out=False)
    except Exception as e:
        message_service.exception('get_groups', repr(e))
        return None


def delete_group_by_id(pk):
    try:
        Group.query.filter_by(id=pk).delete()
        db.session.commit()

        return True
    except Exception as e:
        message_service.exception('delete_group_by_id', repr(e))
        return False
