from flask import url_for, request


def pagination(accounts, page, per_page):
    # build the pagination metadata to include in the response
    pages = {'page': page, 'per_page': per_page, 'pages': accounts.pages}
    if accounts.has_prev:
        pages['prev_url'] = url_for(request.endpoint, page=accounts.prev_num,
                                    per_page=per_page, _external=True)
    else:
        pages['prev_url'] = None
    if accounts.has_next:
        pages['next_url'] = url_for(request.endpoint, page=accounts.next_num,
                                    per_page=per_page, _external=True)
    else:
        pages['next_url'] = None
    pages['first_url'] = url_for(request.endpoint, page=1,
                                 per_page=per_page, _external=True)
    pages['last_url'] = url_for(request.endpoint, page=accounts.pages,
                                per_page=per_page, _external=True)
    return pages