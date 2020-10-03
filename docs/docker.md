# docker

    - To download and run the latest image on your local run the following commands:
        
        $ docker pull armageddon:1.0.2
        
        $ docker run -it -p 8090:4000 pppm/armageddon:1.0.2
        
        Port 4000 is exposed from the container.
        Port 8090 is of local machine and can be different.

### Build docker and run the image

    - Navigate to root of the project
    
    - The following command creates an image in your local machine:
        $ docker build --tag <imagename>:<tagname> .
        
    - The following command create a container and run it from the image:
        $ docker run -it -p 8090:4000 --name <nameYouWantOnLocalMachine> <imagename>:<tagname>
    
    - To pass environment variables:
        $ docker run -e ENV_VAR_1=1 -e ENV_VAR_2=2 -it -p 8090:4000 --name <nameYouWantOnLocalMachine> <imagename>:<tagname>
        
### Build docker and publish to docker hub

    - Repeat first two steps from "Build docker and run the image" section
    
    - The following command will push the image to docker hub
        $ docker push <your_username>/<imagename>:<tagname>
         
### Download docker image from Docker Hub and run the image
    
    - The following command downloads the image from docker hub
    
        $ docker pull <your_username>/<imagename>:<tagname>
        
    - Run the docker run command as mentioned in "Build docker and run the image" section.


### Using curl
    - curl get http://127.0.0.1:8090/tests/<filename.py>
    - curl get http://127.0.0.1:8090/tests/<filename.py>::<test_func_name>



- [HomePage](../README.md)
