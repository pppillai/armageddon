# How to write Tests

### Structure of the framework:
  - clients package: Contains all the client api as sub pacakages.
  - utils package: Utility methods.
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

### Running the Tests:
  - make sure virtual env is running.
  - In a terminal in the root of armageddon project run the following command:
    - pytest --html report.html tests/

- [HomePage](../README.md)