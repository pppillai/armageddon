# How to write Tests

### Structure of the framework:
  - clients package: Contains all the client api as sub packages.
  - utils package: Contains Utility methods.
  - docs: 
  - tests package: Contains tests files and response dataclasses.

### Writing Tests:

  #### New Api
    - Create a new package.
    - Write a class and implement the exposed endpoints.
    - In the __init__.py file add the class.
    - In conftest.py in tests folder add a fixture to return an instance of the class.
    - In tests folder add tests.
    
  #### New Endpoint for existing api
    - In the class for the api add the method exposing the endpoint.


- [HomePage](../README.md)