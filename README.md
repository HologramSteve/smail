Program Documentation
This documentation provides an overview of the program functionality, including how it works and the purpose of each file. It also includes instructions for using the program and example usage.

Table of Contents
Overview
Files
main.py
dbhandler.py
Usage
Example Usage
Overview<a name="overview"></a>
The program is a server application that handles email-related functionality. It allows users to connect, retrieve emails, add new emails, and perform other related operations. The program consists of two main files: main.py and dbhandler.py.

Files<a name="files"></a>
main.py<a name="mainpy"></a>
main.py is the entry point of the program. It starts the server and handles the communication between clients and the server. The file contains the following sections:

Configuration: This section includes the configuration variables such as projectid, username, and sessionid. These variables are used for connecting to the cloud and establishing the session.

Starting code: This section initializes the necessary components for the server to function. It imports the required modules and establishes a connection to the cloud project using the provided session ID and username. It also creates an instance of the scratch3.CloudRequests class to handle incoming requests.

Requests: This section defines several request handlers that handle different types of requests received from clients. The requests include connecting with a username, retrieving user-specific emails, retrieving emails by ID, and adding new emails. Each request handler performs specific operations and returns the corresponding data.

End code: This section defines an event handler for the server's on_ready event, which is triggered when the server is ready to receive requests. It also starts the server by calling the run method.

dbhandler.py<a name="dbhandlerpy"></a>
dbhandler.py is a module that provides functions for accessing and manipulating email data in the database. It contains the following functions:

getmail: This function retrieves an email from the database based on the provided ID. It reads the database file, db.json, and extracts the relevant information for the specified email ID. The function returns the email's details in a list.

add_email: This function adds a new email to the database. It takes email information as input, splits it into title, content, author, and sendto fields, and creates a new email object. The function then updates the db.json file by appending the new email object to the database.

Usage<a name="usage"></a>
To use the program, follow these steps:

Ensure you have the necessary dependencies installed. The program requires the scratchattach and json modules.

Set up the configuration variables in main.py according to your environment. Provide the appropriate values for projectid, username, and sessionid.

Ensure the db.json file exists and is accessible by the program. This file serves as the database for storing email information.

Run the program by executing main.py using a Python interpreter.

Once the server starts, it will listen for incoming requests and respond accordingly.

Example Usage<a name="example-usage"></a>
Here's an example of how to use the add_email function in dbhandler.py to add a new email:
