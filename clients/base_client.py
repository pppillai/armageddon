from json import JSONDecodeError
import requests


class BaseClient:

    def __init__(self):
        self.base_url = ""
        self.requests = requests.Session()

    @staticmethod
    def parse_response(response):
        try:
            response_body = response.json()
        except JSONDecodeError:
            response_body = response.text
        return response.status_code, response_body


