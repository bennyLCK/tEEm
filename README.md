# tEEm
## LifeHack 2024 Project

## Project Description
This project is a part of the LifeHack 2024 Hackathon. The project is a web application that handles user interactions with regards to querying a database. The main aim of the project was to allow authenticated requests for database queries and also for the responses themselves to be encrypted in the information transfer process to prevent attackers from accessing the database without authorization and sniffing the responses themselves if the network is compromised.

## Project Features

### Implemented Features (Backend)

1. Handling of database queries
   1. The project allows users to interact with the database for information using `POST, GET, PUT, DELETE` requests. (running app.py first followed by running the req.py file after populating it with requests. Currently, the state of the SQLite database can be viewed by going to "http://localhost:5000/patients" in a browser after running the app.py followed by req.py. The success or failure of the requests can be seen in the terminal where the app.py is running.)
   2. A suitable error message would be returned upon an invalid request.
   3. There are currently no mechanisms to encrypt responses and to authenticate user requests due to time constraints.

### Planned Features (Frontend and Backend)

1. Implementing a frontend for the project
   1. The frontend would be implemented using ReactJS.
   1. The frontend would also allow users to authenticate themselves before making requests to the database.
   1. The frontend would also allow users to opt in to encrypting responses to prevent attackers from sniffing the responses if the network is compromised.


1. Implementing the encryption and authentication mechanisms for the project
   1. The project would implement a mechanism to encrypt responses to prevent attackers from sniffing the responses if the network is compromised via authenticated-encryption schemes like the AES GCM mode of operation encryption protocol.
   1. The project would also implement a mechanism to authenticate user requests to prevent unauthorized access to the database via setting up JWT tokens for authorized users.
