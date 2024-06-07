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

# and Now we are inserting many documents(records)



def insertmanydocuments():
    collection=productvar.person_collection                                #person_collection is name of collection
    first_names=["Tim","Stenven","Charlie","Kevin","Gwen"]
    last_names=["Rusith","Tennyson","Cater","Trump","Geral"]
    ages=[21,34,56,32,19]

    docs=[]
    for firstname, lastname, age in zip(first_names,last_names,ages):
        doc={"first_name":firstname,"last_name":lastname,"age":age}
        docs.append(doc)

    collection.insert_many(docs)


insertmanydocuments()
    
    