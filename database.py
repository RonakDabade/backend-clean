from pymongo import MongoClient
import certifi

MONGO_URL = "mongodb+srv://admin:admin@cluster0.s4rew4c.mongodb.net/?appName=Cluster0"

client = MongoClient(
    MONGO_URL,
    tls=True,
    tlsCAFile=certifi.where()
)

db = client["user_db"]
users_collection = db["users"]

print("mongo connected")