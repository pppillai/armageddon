from json import JSONDecodeError
import requests


class BaseClient:
    """
    This client can be used to store common base urls and other config stuff.
    """
    def __init__(self):
        self.base_url = ""
        self.requests = requests.Session()


