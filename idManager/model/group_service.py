from idManager.model import message_service
from idManager.model.database.db_schema import GroupSchema
from idManager.model.integration import group_data
from idManager.model.util_service import pagination
from idManager.settings import MSG_GROUP_ALREADY_REGISTERED, MSG_GROUP_SET, MSG_GROUP_DELETED

# region Schema
group_schema = GroupSchema(only=('name','id'))
get_groups_schema = GroupSchema(many=True, only=('id', 'name', 'url'))
get_group_schema = GroupSchema(only=('id', 'name', 'url', 'created_at'))
# endregion


def group_register_ver_1(name):
    group = group_data.get_group_by_name(name)

    if group is None:
        if group_data.register_group(name):
            group = group_data.get_group_by_name(name)

            return {'message': MSG_GROUP_SET,
                    'group': group_schema.dump(group),
                    'http_status_code': 201}
        else:
            message_service.error_500('account_register_ver_1')

    else:
        message_service.error_400('account_register_ver_1: ' + MSG_GROUP_ALREADY_REGISTERED, MSG_GROUP_ALREADY_REGISTERED)


def get_groups_ver_1(page, per_page):
    groups = group_data.get_groups(page, per_page)

    pages = pagination(groups, page, per_page)

    return {'groups': get_groups_schema.dump(groups.items),
            'total': groups.total,
            'pages': pages,
            'http_status_code': 200}


def get_group_by_id_ver_1(pk):
    group = group_data.get_group_by_id(pk)

    if group is not None:
        return {'group': get_group_schema.dump(group),
                'http_status_code': 200}
    else:
        message_service.error_404('get_account_by_id_ver_1')


def delete_group_by_id_ver_1(pk):
    group = group_data.get_group_by_id(pk)
    if group is not None:
        if group_data.delete_account_by_id(pk):
            return {'message': MSG_GROUP_DELETED,
                    'group': group_schema.dump(group),
                    'http_status_code': 202}
        else:
            message_service.error_500('delete_group_by_id_ver_1')
    else:
        message_service.error_404('delete_group_by_id_ver_1')
