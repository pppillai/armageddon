import pytest
import logging
import time


# client fixtures

@pytest.fixture(scope="session")
def sbdb_close_approach_data_client():
    from clients.nasa import SBDBCloseApproachDataClient
    return SBDBCloseApproachDataClient()


@pytest.fixture(autouse=True)
def logger(request):
    log = logging.getLogger(__name__)
    log.info(f"\nStarting Test : {request.node.name} : {time.asctime(time.localtime())}\n")
    return log