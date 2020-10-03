
from clients.base_client import BaseClient
from clients.config import Config
from clients.utils.parse import parse_response
import os


class HelloServiceClient(BaseClient):
    """
    Client for hello svc.
    Project is described here:
    https://github.com/pppillai/pp-eye
    """

    def __init__(self):
        super().__init__()

        self.ip = Config.KUBECLUSTERIP
        self.port = Config.NODEPORTPORT

        if not self.ip:
            self.ip = os.environ.get("KUBECLUSTERIP")

        if not self.port:
            self.port = os.environ.get("NODEPORTPORT")

    def get(self, name=None):
        """

        :param name: Any valid string
        :return: status, text tuple
        """
        if self.ip is None:
            assert False, "Environment variable KUBECLUSTERIP not set"
        if self.port is None:
            assert False, "Environment variable NODEPORTPORT not set"

        url = f"http://{self.ip}:{self.port}/{name}" if name else f"http://{self.ip}:{self.port}"

        response = self.requests.get(url=url, timeout=Config.TIMEOUT)

        status, parsed_resp = parse_response(response)

        return status, parsed_resp