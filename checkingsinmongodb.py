
"""
Python MongoDB Create Database
Creating a Database
To create a database in MongoDB, start by creating a MongoClient object, then specify a connection URL with the correct ip address and the name of the database you want to create.

MongoDB will create the database if it does not exist, and make a connection to it.

"""
#Create a database called "mydatabase":

from dotenv import load_dotenv, find_dotenv
import os
import pprint

from pymongo import MongoClient
load_dotenv(find_dotenv())

password=os.environ.get("MONGODB_PWD")

#dbusername-aasvakoodalarasan & password- is in .env file
connectionstring=f"mongodb+srv://aasvakoodalarasan:{password}@cluster2.4hvpznb.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connectionstring)

#Database and Collection(Table) were created through mongo atlas( in browser) and so after creation,we are checking db and collection below

#Checking databases
dbs=client.list_database_names()
print(dbs)

testdb=client.mydatabase                     #mydatabase is name of database 

#Checking Collections(table)
collections=testdb.list_collection_names()
print(collections)