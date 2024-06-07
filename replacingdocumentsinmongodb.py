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

#Now We gonna replace documents(records)
def replacedocuments(person_id):
    from bson.objectid import ObjectId
    _id=ObjectId(person_id)

    new_doc={
        "first_name":"replacedfirstname",
        "last_name":"replacedlastname",
        "age":100
    }
    person_collectionvar.replace_one({"_id":_id}, new_doc)

replacedocuments("64f6dabee89b4acfe8db6da0")