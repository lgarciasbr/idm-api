from flask import request as requests, jsonify as json


# region Home
def about():
    # Welcome
    # GET http://127.0.0.1:5000/

    try:
        response = requests.get(
            url="http://127.0.0.1:5000/",
        )
        print('about')
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))

        return response

    except requests.exceptions.RequestException:
        print('about - HTTP Request failed!')
        return None
# endregion


# region Account
def register_account(header, data):
    # Register
    # POST http://127.0.0.1:5000/accounts/

    try:
        response = requests.post(
            url="http://127.0.0.1:5000/accounts/",
            headers=header,
            data=json.dumps(data)
        )
        print('register_account')
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))

        return response

    except requests.exceptions.RequestException:
        print('register_account - HTTP Request failed!')
        return None


def delete_account_by_id(pk, header):
    # Delete User
    # DELETE http://127.0.0.1:5000/accounts/38

    try:
        response = requests.delete(
            url="http://127.0.0.1:5000/accounts/" + pk,
            headers=header
        )
        print('delete_account_by_id')
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))

        return response

    except requests.exceptions.RequestException:
        print('delete_account_by_id - HTTP Request failed!')
        return None


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
# endregion


# region Auth
def auth_login(header, data):
    # Login
    # POST http://127.0.0.1:5000/auth/

    try:
        response = requests.post(
            url="http://127.0.0.1:5000/auth/",
            headers=header,
            data=json.dumps(data)
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))

        return response

    except requests.exceptions.RequestException:
        print('auth_login - HTTP Request failed!')
        return None


def auth_is_valid(header):
    # Is this token valid?
    # GET http://127.0.0.1:5000/auth/

    try:
        response = requests.get(
            url="http://127.0.0.1:5000/auth/",
            headers=header,
        )
        print('auth_is_valid')
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))

        return response

    except requests.exceptions.RequestException:
        print('auth_is_valid - HTTP Request failed!')
        return None


def auth_logout(header):
    # Logout
    # DELETE http://127.0.0.1:5000/auth/

    try:
        response = requests.delete(
            url="http://127.0.0.1:5000/auth/",
            headers=header,
        )
        print('auth_logout')
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))

        return response

    except requests.exceptions.RequestException:
        print('auth_logout - HTTP Request failed!')
        return None
# endregion
