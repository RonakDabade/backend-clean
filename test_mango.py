from pymongo import MongoClient

MONGO_URL = "mongodb+srv://admin:admin@cluster0.s4rew4c.mongodb.net/?appName=Cluster0"

client = MongoClient(MONGO_URL)
db = client["test_db"]

print("MongoDB Atlas connected!")
