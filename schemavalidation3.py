from dotenv import load_dotenv, find_dotenv
from datetime import datetime as dt
import os
import pprint

from pymongo import MongoClient
load_dotenv(find_dotenv())

password=os.environ.get("MONGODB_PWD")

#dbusername-aasvakoodalarasan & password- is in .env file
connectionstring=f"mongodb+srv://aasvakoodalarasan:{password}@cluster2.4hvpznb.mongodb.net/?retryWrites=true&w=majority"

client=MongoClient(connectionstring)

productvar=client.production


#Inserting Datas for author collection(table):

authors=[
    {
        "first_name":"Koodalarasan",
        "last_name":"Mohandas",
        "date_of_birth":dt(2000,7,20)
    },
    {
        "first_name":"Muthu",
        "last_name":"Kumar",
        "date_of_birth":dt(2001,8,21)
    },
    {
        "first_name":"Saiful",
        "last_name":"Islam",
        "date_of_birth":dt(2002,9,22)
    },

]

author_collection=productvar.author
authors=author_collection.insert_many(authors).inserted_ids   #inserted_ids is an built-in property.


#Inserting Datas for book collection(table):

books=[
{
    "title":"MongoDB Advanced Tutorial",
    "authors":[authors[0]],
    "publish_date":dt.today(),
    "type":"Non-fiction",
    "copies":50

},
{
    "title":"Python Advanced Tutorial",
    "authors":[authors[1]],
    "publish_date":dt(2023,7,10),
    "type":"Non-fiction",
    "copies":15

},
{
    "title":"React Advanced Tutorial",
    "authors":[authors[2]],
    "publish_date":dt(2023,7,23),
    "type":"Non-fiction",
    "copies":52

}

]

book_collection=productvar.book
books=book_collection.insert_many(books).inserted_ids

#continues to advancedqueries.py