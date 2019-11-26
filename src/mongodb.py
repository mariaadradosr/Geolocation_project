
import os
import config
import pymongo
from pymongo import MongoClient

connectionURL=os.getenv("MONGODB_URL")
client = MongoClient(connectionURL)
print(f"Connected to mongodb in -> {connectionURL}")

def getClient():
    return client

def getCollection(colName, dbName="mibbdd"):   
    db = client[dbName]
    col = db[colName]
    return db, col