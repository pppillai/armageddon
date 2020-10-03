import pytest
import logging
import time


# client fixtures

@pytest.fixture(scope="function")
def sbdb_close_approach_data_client():
    """
    A new instance of SBDBCloseApproachClient object will be returned
    for each test as the fixture is function scoped.
    :return: SBDBCloseApproachDataClient object
    """
    from clients.nasa import SBDBCloseApproachDataClient
    return SBDBCloseApproachDataClient()


@pytest.fixture(scope="function")
def hello_svc_client():
    """
    A new instance of HelloServiceClient object will be returned
    for each test as the fixture is function scoped.
    :return: HelloServiceClient object
    """
    from clients.hello_svc import HelloServiceClient
    return HelloServiceClient()


@pytest.fixture(autouse=True)
def logger(request):
    log = logging.getLogger(__name__)
    log.info(f"\nStarting Test : {request.node.name} : {time.asctime(time.localtime())}\n")
    return log
