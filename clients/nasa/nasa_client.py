from clients.base_client import BaseClient
from urllib.parse import urlencode
from clients.utils.parse import parse_response, stringify_query_param
import copy

DEFAULT_QUERY_DICT = {
                        "date-min": "now",
                        "date-max": "+60",
                        "dist-max": "0.05",
                        "neo": True,
                        "body": "Earth",
                        "sort": "date"
                    }


class SBDBCloseApproachDataClient(BaseClient):
    """
    This class represents close approach data api.
    Implement all the methods exposed by the api.

    _version: current version is 1.1
    _query_params: default values exposed by the server.
    """
    def __init__(self):
        super().__init__()
        self._base_url = "https://ssd-api.jpl.nasa.gov/cad.api"
        self._version = '1.1'
        self._query_params = copy.deepcopy(DEFAULT_QUERY_DICT)

    def get(self, encode=True):
        """
        Get method exposed by the api
        :param encode: default value True, use this to either encode url params or pass as in.
        :return: status and json parsed response.
        """
        if len(self._query_params) > 0:
            if encode:
                url = f"{self._base_url}?{urlencode(self._query_params)}"
            else:
                url = f"{self._base_url}?{stringify_query_param(self._query_params)}"
        else:
            url = self._base_url

        response = self.requests.get(url=url, json=self._query_params)
        status, parsed_resp = parse_response(response)

        assert parsed_resp['signature']['version'] == self._version

        return status, parsed_resp

    def add_query_param(self, **kwargs):
        """
        Use this method to add query params that will be appended to the url.
        :param kwargs: accepts params keyword arguments.
        """
        self._query_params.update(kwargs)

    def add_query_params(self, query_dict):
        """
        Use this method to add multiple query params at once.
        :param query_dict: dict object with query params.
        """
        self._query_params.update(query_dict)

    def clear_all_query_param(self):
        """
        Use this method to clear all the default query params.
        """
        self._query_params.clear()


