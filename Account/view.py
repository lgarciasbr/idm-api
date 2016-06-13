from lib.json import json

# todo implementar o retorno com xml

@json
def message_json(value):
    if 'http_code_status' in value:
        del value['http_code_status']

    return value
