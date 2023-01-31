# Mircroservice-1
Converts a given city of a given state to Zip Code
1st Method: 
Run the python file
Use this address to see the zipcode for the given city and state: http://127.0.0.1:8000/zipcode?city=Sunnyvale&state=CA
Change the city and state to see the desired zipcode.

2nd Method:
go to the project directory and build the docker image using the command:
docker build -t zipcode:1.0 .
After building the image run the container on port 5000. The command is in the line below:
docker run -d -p 5000:8000 --name city_to_zipCode zipcode:1.0 
Make sure this port is available on your host machine, if not change port and use one which is available. In that case use that specific port address to view the 
result on your browser. 
Use this address to see the result on your browser: http://127.0.0.1:5000/zipcode?city=Sunnyvale&state=CA
Again you can make changes to the city and state to view your desired zip code.

Below is the link of the docker image in docker hub, you can pull it from here:
https://hub.docker.com/repository/docker/wasifafridi25/microservice1/general

![Screenshot (260)](https://user-images.githubusercontent.com/122373939/215633750-56a3aacc-adc1-4bed-884a-5d42afd93634.png)
![Screenshot (262)](https://user-images.githubusercontent.com/122373939/215633803-25c27fd9-fe7e-4033-b16b-3e4ababd22da.png)
![Screenshot (261)](https://user-images.githubusercontent.com/122373939/215633811-c177e9cf-f224-4761-a920-91d302eed3f3.png)
![Screenshot (264)](https://user-images.githubusercontent.com/122373939/215716891-8002ecfa-015b-4998-8777-aebdd411b826.png)
![Screenshot (265)](https://user-images.githubusercontent.com/122373939/215716895-64bea1c5-6327-4610-8d5a-c93bd688889c.png)
![Screenshot (263)](https://user-images.githubusercontent.com/122373939/215716898-20ac7202-1e64-4e6a-a2b5-f44349b211de.png)
