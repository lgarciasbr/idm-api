from flask import jsonify


def register_group(http_status_code, group, message):
    view = jsonify({'status_code': http_status_code, 'message': message, 'group': group.data})

    return view


def get_groups(groups, total, pages, http_status_code):

    view = jsonify({'groups': groups.data,
                    'total': total,
                    'pages': pages,
                    'status_code': http_status_code})

    return view


def get_group_by_id(http_status_code, group):
    view = jsonify({'status_code': http_status_code, 'group': group.data})

    return view


def delete_group(http_status_code, group, message):
    view = jsonify({'status_code': http_status_code, 'message': message, 'group': group.data})

    return view
