from dotenv import load_dotenv, find_dotenv
import os
import pprint

from pymongo import MongoClient
load_dotenv(find_dotenv())

password=os.environ.get("MONGODB_PWD")

#dbusername-aasvakoodalarasan & password- is in .env file
connectionstring=f"mongodb+srv://aasvakoodalarasan:{password}@cluster2.4hvpznb.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connectionstring)
  

#Creating database and collection(table)
productvar=client.production                              #production is name of database
person_collectionvar=productvar.person_collection         #person_collection is name of collection(table)



def insert_test_doc():
    collection=productvar.person_collection             #person_collection is name of collection(table)

    test_doc1={
        "name":"Mia",
        "type":"test"
    }
    
    collection.insert_one(test_doc1)
    
insert_test_doc()


#In mongodb, only after inserting documents(records)- the mongodb interface will show database and collections(table) and all....
#that's why we inserted the documents(records) within it.
#So don't forget to insert documents(records)within it, inorder to show(create) database and collections and all in mongodb interface.
