LDT take-home challenge

Setup:
- Docker v4.25.0 or greater

Setup command:
````
docker-compose up --build
````
Docs and usage:
````
http://localhost:5000/docs#/
````
Run tests:
````
docker exec ldt-api pytest
````
Notes for improvement:

I wasn't able to complete the challenge fully, I spent a decent amount of time getting the ideal project setup and trying to parse the json into an actual db but eventually realised I will have to cut this corner. Input validation is another corner I had to skip for the POST call to save time. Test coverage could also be improved in my opinion given more time. Exception handling is another thing that is a must for a backend but I had to skip this to save time.
