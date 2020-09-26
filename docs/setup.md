# Setup

### Prerequisite
- Install Python3 ![python3](https://realpython.com/installing-python/)
- Install virtual environment ![venv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

### Clone the repository
  - For SSH: 
    
    `git clone git@github.com:pppillai/armageddon.git`
    
  - For HTTP: 

    `git clone https://github.com/pppillai/armageddon.git`
    
### Steps to run test locally without docker container
 
    $ cd <root_of_armageddon>
    $ python3 -m venv nameyouwant
    $ source nameyouwant/bin/activate
    $ pip install --editable .
    $ pytest --html=report.html tests
    
    
### Steps to run the test locally with docker container
    
    
- [HomePage](../README.md)