
from pymongo import MongoClient
from pprint import pprint

# Provide the mongodb atlas url to connect python to mongodb using pymongo
CONNECTION_STRING = "mongodb+srv://KobraPy:GTrczxSpBqfqDyOI@cluster0.ltxpi0z.mongodb.net/test"

# Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient

client = MongoClient(CONNECTION_STRING)

# Create the database for our example (we will use the same database throughout the tutorial
#print(client.list_database_names())

database = client["mongodbVSCodePlaygroundDB"]


collection_sales = database["sales"]

collection_sales.insert_one({"teste1":123456})

def print_collection(collec:'testeando'):
    for doc in list(collec.find()):
        print(doc)

print_collection(collec=collection_sales)

