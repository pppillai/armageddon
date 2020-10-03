# Quick Start


* Open a new Terminal
    > $ docker pull pppm/armageddon:1.0.3
    
    > $ docker run -e KUBECLUSTERIP=??? -e NODEPORTPORT=??? -it -p 8090:4000 pppm/armageddon:1.0.3
    
        - KUBECLUSTERIP AND NODEPORTPORT are required to run hello svc tests.
        - Replace ??? with actual values. 
        
    [hello service project page](https://github.com/pppillai/pp-eye)

* Open browser
    > http://127.0.0.1:8090

[HomePage](../README.md)