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


#Now we gonna update document(record) in it
def updatedocuments(person_id):
    from bson.objectid import ObjectId

    _id=ObjectId(person_id)

    all_updates={
        "$set":{"new_field":True},
        "$inc":{"age":1},
        "$rename":{"first_name":"FirstName","last_name":"LastName"}
    }
    person_collectionvar.update_one({"_id":_id}, all_updates)

updatedocuments("64f6dabee89b4acfe8db6da0")