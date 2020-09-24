from json import JSONDecodeError


def parse_response(response):
    try:
        response_body = response.json()
    except JSONDecodeError:
        response_body = response.text
    return response.status_code, response_body


def stringify_query_param(query_params):
    params = []
    for key, value in query_params.items():
        params.append(str(key) + "=" + str(value))
    return "&".join(params)