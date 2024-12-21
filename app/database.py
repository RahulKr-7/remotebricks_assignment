from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017"  # Replace with your MongoDB URI if using Atlas
client = MongoClient(MONGO_URI)
db = client["remobricks_db"]  # Replace "user_database" with your database name
