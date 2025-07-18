from pymongo import MongoClient
from config import MONGO_URI, DB_NAME, COLLECTION_NAME

# Extended timeouts and retries
client = MongoClient(
    MONGO_URI,
    serverSelectionTimeoutMS=20000,  # 20 seconds
    connectTimeoutMS=20000,
    socketTimeoutMS=20000,
    retryWrites=True
)

db = client[DB_NAME]
collection = db[COLLECTION_NAME]

def store_issue(data: dict):
    collection.insert_one(data)

def get_all_issues():
    return list(collection.find({}, {"_id": 0}))
