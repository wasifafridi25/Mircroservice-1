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

