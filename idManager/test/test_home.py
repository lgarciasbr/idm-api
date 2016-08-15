import json
import pytest
from idManager.test import records


@pytest.mark.parametrize(("header", "data", "expected"), [
    (records.header_empty(), records.data_empty(), 200),
    (records.header_empty_content_type(), records.data_empty(), 200),
    (records.header_content_type(), records.data_empty(), 200),
    (records.header_invalid_content_type(), records.data_empty(), 400),
])
def test_about_get(client, header, data, expected):
    response = client.get('/',
                          headers=header,
                          data=json.dumps(data))

    # json.loads(response.data.decode('utf-8'))['description']

    assert response.status_code == expected


@pytest.mark.parametrize(("header", "data", "expected"), [
    (records.header_empty(), records.data_empty(), 405),
    (records.header_empty_content_type(), records.data_empty(), 405),
    (records.header_content_type(), records.data_empty(), 405),
    (records.header_invalid_content_type(), records.data_empty(), 405),
])
def test_about_post(client, header, data, expected):
    response = client.post('/',
                           headers=header,
                           data=json.dumps(data))

    assert response.status_code == expected


@pytest.mark.parametrize(("header", "data", "expected"), [
    (records.header_empty(), records.data_empty(), 405),
    (records.header_empty_content_type(), records.data_empty(), 405),
    (records.header_content_type(), records.data_empty(), 405),
    (records.header_invalid_content_type(), records.data_empty(), 405),
])
def test_about_put(client, header, data, expected):
    response = client.put('/',
                          headers=header,
                          data=json.dumps(data))

    assert response.status_code == expected


@pytest.mark.parametrize(("header", "data", "expected"), [
    (records.header_empty(), records.data_empty(), 405),
    (records.header_empty_content_type(), records.data_empty(), 405),
    (records.header_content_type(), records.data_empty(), 405),
    (records.header_invalid_content_type(), records.data_empty(), 405),
])
def test_about_delete(client, header, data, expected):
    response = client.delete('/',
                             headers=header,
                             data=json.dumps(data))

    assert response.status_code == expected
