# armageddon

- [Setup](/docs/setup.md)

- [Docker](/docs/docker.md)

- [How to write tests](/docs/tests.md)

- [Screenshots](/docs/screenshot.md)

"armageddon" is a api tool to test public apis.
- Release (2020-September-27)
    - tests for SBDB Close-Approach Data API are implemented.

- Release (2020-October-04)
    - tests for hello svc (kubernetes/docker) api ared implemented.


Tests are implemented in Python 3.8 version.

Libraries used as follows:
- [requests](https://requests.readthedocs.io/en/master/): for making http calls.
- [jsons](https://pypi.org/project/jsons/): for parsing json to data classes.
- [pytest](https://docs.pytest.org/en/stable/): framework for running tests.
- [flask](https://flask.palletsprojects.com/en/1.1.x/): framework for web.
- [docker](https://www.docker.com/): to containerize the tool.
- [gunicorn](https://gunicorn.org/): wsgi server to serve the flask app.
