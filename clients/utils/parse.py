from json import JSONDecodeError


def parse_response(response):
    """
    Use this function to parase response object into json
    :param response:
    :return: status code and parsed response body
    """
    try:
        response_body = response.json()
    except JSONDecodeError:
        response_body = response.text
    return response.status_code, response_body


def stringify_query_param(query_params):
    """
    Using this to append key value to url
    :param query_params:
    :return: string in form of key=value&key1=value1
    """
    params = []
    for key, value in query_params.items():
        params.append(str(key) + "=" + str(value))
    return "&".join(params)