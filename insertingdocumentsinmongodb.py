from dotenv import load_dotenv, find_dotenv
import os
import pprint

from pymongo import MongoClient
load_dotenv(find_dotenv())

password=os.environ.get("MONGODB_PWD")

#dbusername-aasvakoodalarasan & password- is in .env file
connectionstring=f"mongodb+srv://aasvakoodalarasan:{password}@cluster2.4hvpznb.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connectionstring)


# The Database and Collection(Table) were used here which were created through mongo atlas( in browser).
#Not databases of creatingdatabaseandcollection.py



testdb=client.mydatabase                     #mydatabase is name of database 


# and Now we are inserting documents(records)

def insert_test_doc():
    collection=testdb.customers              #customers is name of collection(table)

    test_doc1={
        "name":"Ria",
        "type":"test"
    }
    
    collection.insert_one(test_doc1)
    
insert_test_doc()


#To get know whether the document(record) is inserted or not, use inserted_id to display is to confirm insertion

def insert_test_doc1():
    collection=testdb.customers

    test_doc2={
        "name":"Zia",
        "type":"test"
    }
    
    inserted_id=collection.insert_one(test_doc2).inserted_id
    print(inserted_id)
    

insert_test_doc1()

