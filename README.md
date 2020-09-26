# armageddon

- ![Setup](/docs/setup.md)

- ![Docker](/docs/docker.md)

- ![How to write tests](/docs/tests.md)

"armageddon" is a api tool to test public apis.
As of now tests for SBDB Close-Approach Data API api is implemented.

Tests are implemented in Python3.8 version.
Libraries used as follows:
- ![requests](https://requests.readthedocs.io/en/master/): for making http calls.
- ![jsons](https://pypi.org/project/jsons/): for parsing json to data classes.
- ![pytest](https://docs.pytest.org/en/stable/): framework for running tests.
- ![flask](https://flask.palletsprojects.com/en/1.1.x/): framework for web.
- ![docker](https://www.docker.com/): to contanizer the tool.