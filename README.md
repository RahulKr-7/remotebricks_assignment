**Objective**
This project provides APIs for user management, including registration, login, ID linking, data joins, and chain delete functionalities, implemented using FastAPI and MongoDB.

**Features**
1. User Registration: Register users with a username, email, and hashed password.
2. User Login: Authenticate users using their email and password.
3. Linking External ID: Associate an external ID with a user's account.
4. Joins: Retrieve combined data from multiple MongoDB collections.
5. Chain Delete: Delete a user and all related data across collections.

**Technologies Used**
1. Framework: FastAPI
2. Database: MongoDB

**Libraries:**
1. pymongo: MongoDB client for Python
2. passlib: For password hashing
3. pytest: For testing

**Prerequisites**
1. Install Python 3.10 or later.
2. Install MongoDB and ensure it is running.
3. Install required Python libraries:
*pip install fastapi pymongo passlib uvicorn*

**Setup Instructions**
1. Clone this repository:
git clone https://github.com/RahulKr-7/remotebricks_assignment.git

2. Navigate to the project directory:
cd remotebricks_assignment

3. Start the FastAPI server:
uvicorn main:app --reload

4. Access the API documentation at:
http://127.0.0.1:8000/docs