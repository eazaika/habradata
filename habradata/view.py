from pymongo import MongoClient

client = MongoClient()
db = client.habrahabr
coll = db.titles

def data(self):
    return coll.find()
