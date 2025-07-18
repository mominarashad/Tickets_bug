# test_connection.py
from pymongo import MongoClient

uri = "mongodb+srv://mominarashad137:YHfYRbcr2FyyoWQB@cluster0.vsxvet0.mongodb.net/?retryWrites=true&w=majority"

try:
    client = MongoClient(uri)
    print(client.list_database_names())  # Try a basic operation
except Exception as e:
    print("Connection error:", e)
