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


author_validator = {
      "$jsonSchema": {
         "bsonType": "object",
         "required": [ "first_name", "last_name", "date_of_birth" ],
         "properties": {
            "first_name": {
               "bsonType": "string",
               "description": " must be a string and is required"
            },
            "last_name": {
               "bsonType": "string",
               "description": " must be a string and is required"
            },
            "date_of_birth": {
               "bsonType": "date",
               "description": " must be a date and is required"
            },
         }
      }
   }

try:
   productvar.create_collection('author')

except Exception as e:
   print(e)

productvar.command("collMod","author",validator=author_validator)

#continues to schemavalidation3.py