import json
import pytest
from tests import records
from flask import current_app


@pytest.mark.parametrize(("header", "data", "deliverability", "expected"), [
    (records.header_empty(), records.data_email_pwd(), False, 201),
    (records.header_no_content_type_ver(), records.data_email_pwd(), False, 201),
    (records.header_content_type_no_ver(), records.data_email_pwd(), False, 201),
    (records.header_empty_content_type_ver(), records.data_email_pwd(), False, 201),
    (records.header_content_type_empty_ver(), records.data_email_pwd(), False, 201),
    (records.header_invalid_content_type_ver(), records.data_email_pwd(), False, 400),
    (records.header_content_type_invalid_ver(), records.data_email_pwd(), False, 400),
    (records.header_content_type_ver(), records.data_deliverability_email_pwd(), True, 400),
    (records.header_content_type_ver(), records.data_email_pwd(), False, 201),
    (records.header_content_type_ver(), records.data_empty(), False, 400),
    (records.header_content_type_ver(), records.data_no_email_pwd(), False, 400),
    (records.header_content_type_ver(), records.data_empty_email_pwd(), False, 400),
    (records.header_content_type_ver(), records.data_invalid_email_pwd(), False, 400),
    (records.header_content_type_ver(), records.data_email_no_pwd(), False, 400),
    (records.header_content_type_ver(), records.data_email_empty_pwd(), False, 400),
])
def test_register_account(client, header, data, deliverability, expected):
    current_app.config['CHECK_EMAIL_DELIVERABILITY'] = deliverability

    response = client.post('/accounts/',
                           headers=header,
                           data=json.dumps(data))

    assert response.status_code == expected


def test_try_register_a_registered_account(client):
    headers = records.header_content_type_ver()
    data = records.data_email_pwd()

    client.post('/accounts/',
                headers=headers,
                data=json.dumps(data)
                )

    response_second = client.post('/accounts/',
                                  headers=headers,
                                  data=json.dumps(data)
                                  )

    assert response_second.status_code == 400


# wrong ver
# token - 0 (no token), 1 (valid token), 2 (invalid token)
# pk - 0 (no pk), 1 (valid pk), 2 (invalid pk)
@pytest.mark.parametrize(("header", "token", "pk", "expected"), [
    (records.header_empty(), 0, 0, 405),
    (records.header_empty(), 0, 1, 400),
    (records.header_empty(), 0, 2, 400),
    (records.header_empty(), 1, 0, 405),
    (records.header_empty(), 1, 1, 202),
    (records.header_empty(), 1, 2, 404),
    (records.header_empty(), 2, 0, 405),
    (records.header_empty(), 2, 1, 403),
    (records.header_empty(), 2, 2, 403),
    (records.header_no_content_type_ver(), 0, 0, 405),
    (records.header_no_content_type_ver(), 0, 1, 400),
    (records.header_no_content_type_ver(), 0, 2, 400),
    (records.header_no_content_type_ver(), 1, 0, 405),
    (records.header_no_content_type_ver(), 1, 1, 202),
    (records.header_no_content_type_ver(), 1, 2, 404),
    (records.header_no_content_type_ver(), 2, 0, 405),
    (records.header_no_content_type_ver(), 2, 1, 403),
    (records.header_no_content_type_ver(), 2, 2, 403),
    (records.header_content_type_no_ver(), 0, 0, 405),
    (records.header_content_type_no_ver(), 0, 1, 400),
    (records.header_content_type_no_ver(), 0, 2, 400),
    (records.header_content_type_no_ver(), 1, 0, 405),
    (records.header_content_type_no_ver(), 1, 1, 202),
    (records.header_content_type_no_ver(), 1, 2, 404),
    (records.header_content_type_no_ver(), 2, 0, 405),
    (records.header_content_type_no_ver(), 2, 1, 403),
    (records.header_content_type_no_ver(), 2, 2, 403),
    (records.header_empty_content_type_ver(), 0, 0, 405),
    (records.header_empty_content_type_ver(), 0, 1, 400),
    (records.header_empty_content_type_ver(), 0, 2, 400),
    (records.header_empty_content_type_ver(), 1, 0, 405),
    (records.header_empty_content_type_ver(), 1, 1, 202),
    (records.header_empty_content_type_ver(), 1, 2, 404),
    (records.header_empty_content_type_ver(), 2, 0, 405),
    (records.header_empty_content_type_ver(), 2, 1, 403),
    (records.header_empty_content_type_ver(), 2, 2, 403),
    (records.header_content_type_empty_ver(), 0, 0, 405),
    (records.header_content_type_empty_ver(), 0, 1, 400),
    (records.header_content_type_empty_ver(), 0, 2, 400),
    (records.header_content_type_empty_ver(), 1, 0, 405),
    (records.header_content_type_empty_ver(), 1, 1, 202),
    (records.header_content_type_empty_ver(), 1, 2, 404),
    (records.header_content_type_empty_ver(), 2, 0, 405),
    (records.header_content_type_empty_ver(), 2, 1, 403),
    (records.header_content_type_empty_ver(), 2, 2, 403),
    (records.header_invalid_content_type_ver(), 0, 0, 405),
    (records.header_invalid_content_type_ver(), 0, 1, 400),
    (records.header_invalid_content_type_ver(), 0, 2, 400),
    (records.header_invalid_content_type_ver(), 1, 0, 405),
    (records.header_invalid_content_type_ver(), 1, 1, 400),
    (records.header_invalid_content_type_ver(), 1, 2, 400),
    (records.header_invalid_content_type_ver(), 2, 0, 405),
    (records.header_invalid_content_type_ver(), 2, 1, 400),
    (records.header_invalid_content_type_ver(), 2, 2, 400),
    (records.header_content_type_invalid_ver(), 0, 0, 405),
    (records.header_content_type_invalid_ver(), 0, 1, 400),
    (records.header_content_type_invalid_ver(), 0, 2, 400),
    (records.header_content_type_invalid_ver(), 1, 0, 405),
    (records.header_content_type_invalid_ver(), 1, 1, 400),
    (records.header_content_type_invalid_ver(), 1, 2, 400),
    (records.header_content_type_invalid_ver(), 2, 0, 405),
    (records.header_content_type_invalid_ver(), 2, 1, 403),
    (records.header_content_type_invalid_ver(), 2, 2, 403),
    (records.header_content_type_ver(), 0, 0, 405),
    (records.header_content_type_ver(), 0, 1, 400),
    (records.header_content_type_ver(), 0, 2, 400),
    (records.header_content_type_ver(), 1, 0, 405),
    (records.header_content_type_ver(), 1, 1, 202),
    (records.header_content_type_ver(), 1, 2, 404),
    (records.header_content_type_ver(), 2, 0, 405),
    (records.header_content_type_ver(), 2, 1, 403),
    (records.header_content_type_ver(), 2, 2, 403),
])
def test_delete_account_by_id(client, header, token, pk, expected):
    if pk == 1 or token == 1:
        data, headers, pk_value = records.register_account(client)

    if pk == 0:
        pk_value = ''
    elif pk == 2:
        pk_value = '888888888888'

    if token == 1:
        token_value = records.auth_login(client, data, headers)
        header['token'] = token_value
    elif token == 2:
        header['token'] = 'wrong_token'

    response_delete = client.delete('/accounts/' + str(pk_value),
                                    headers=header)

    assert response_delete.status_code == expected


def change_account_password(pk, header, data):
    # Change Password
    # PUT http://127.0.0.1:5000/accounts/38

    try:
        response = requests.put(
            url="http://127.0.0.1:5000/accounts/" + pk,
            headers=header,
            data=json.dumps(data)
        )
        print('change_account_password')
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))

        return response

    except requests.exceptions.RequestException:
        print('change_account_password - HTTP Request failed!')
        return None


def get_accounts(header):
    # Get Users
    # GET http://127.0.0.1:5000/accounts/

    try:
        response = requests.get(
            url="http://127.0.0.1:5000/accounts/",
            headers=header
        )
        print('get_accounts')
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))

        return response

    except requests.exceptions.RequestException:
        print('get_accounts - HTTP Request failed!')
        return None


def get_account_by_id(pk, header):
    # Get User
    # GET http://127.0.0.1:5000/accounts/38

    try:
        response = requests.get(
            url="http://127.0.0.1:5000/accounts/" + pk,
            headers=header
        )
        print('get_account_by_id')
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))

        return response

    except requests.exceptions.RequestException:
        print('get_account_by_id - HTTP Request failed!')
        return None
