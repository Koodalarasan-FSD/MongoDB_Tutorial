from dotenv import load_dotenv, find_dotenv
import os
import pprint

from pymongo import MongoClient
load_dotenv(find_dotenv())

password=os.environ.get("MONGODB_PWD")

#dbusername-aasvakoodalarasan & password- is in .env file
connectionstring=f"mongodb+srv://aasvakoodalarasan:{password}@cluster2.4hvpznb.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connectionstring)

productvar=client.production                              #production is name of database
person_collectionvar=productvar.person_collection         #person_collection is name of collection(table)

#Now We gonna delete documents
def deletedocuments(person_id):
    from bson.objectid import ObjectId
    _id=ObjectId(person_id)

    person_collectionvar.delete_one({"_id":_id})

deletedocuments("64f6ea9b359937ed11729ddb")