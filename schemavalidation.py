from dotenv import load_dotenv, find_dotenv
import os
import pprint

from pymongo import MongoClient
load_dotenv(find_dotenv())

password=os.environ.get("MONGODB_PWD")

#dbusername-aasvakoodalarasan & password- is in .env file
connectionstring=f"mongodb+srv://aasvakoodalarasan:{password}@cluster2.4hvpznb.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connectionstring)

# https://www.youtube.com/watch?v=nYNAH8K_UhI
# https://www.mongodb.com/docs/manual/core/schema-validation/

productvar=client.production                              #production is name of database


book_validator = {
      "$jsonSchema": {
         "bsonType": "object",
         
         "required": [ "title", "authors", "publish_date", "type","copies" ],
         "properties": {
            "title": {
               "bsonType": "string",
               "description": " must be a string and is required"
            },
            "authors": {
               "bsonType": "array",
               "items":{
                  "bsonType": "objectId",
                  "description": " must be an objectid and is required"
               }
            },
            "publish_date": {
               "bsonType": "date",
               "description": " must be a date and is required"
            },
            "type":{
                "enum":["Fiction","Non-Fiction"],
                "description":"can only be one of the enum values and is required"
            },
            "copies":{
               "bsonType":int,
               "minimum":0,
               "description":"must be an integer greater than 0 and is required"
            },
         }
      }
   }


try:
   productvar.create_collection("book")

except Exception as e:
   print(e)

productvar.command("collMod","book", validator=book_validator)

#continues on schemevalidation2.py