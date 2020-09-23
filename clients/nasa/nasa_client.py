from clients.base_client import BaseClient
from urllib.parse import urlencode

query_param = {
    "date-min": "now",
    "date-max": "+60",
    "dist-max": "0.05",
    "neo": True,
    "body": "Earth",
    "sort": "date"
}


class SBDBCloseApproachDataClient(BaseClient):

    def __init__(self):
        super().__init__()
        self._base_path = "https://ssd-api.jpl.nasa.gov/cad.api"
        self._query_param = query_param
        self._version = '1.1'

    def get(self):
        return self._query_param

    def get_close_approach_data(self, encode=True):
        if encode:
            url = f"{self._base_path}?{urlencode(self._query_param)}"
        else:
            url = f"{self._base_path}?{self.stringify_query_param()}"
        r = self.requests.get(url=url, json=self._query_param)
        return self.parse_response(r)

    def add_query_param(self, **kwargs):
        self._query_param.update(kwargs)

    def clear_all_query_param(self):
        self._query_param.clear()

    def stringify_query_param(self):
        s = ""
        for key, value in self._query_param.items():
            s = s + str(key) + "=" + str(value) + "&"
        return s[0:-1]



