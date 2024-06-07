from dotenv import load_dotenv, find_dotenv
from datetime import datetime as dt
import os
import pprint



import pyarrow
from pymongoarrow.api import Schema
from pymongoarrow.monkey import patch_all
import pymongoarrow as pma
from bson import ObjectId
from pymongo import MongoClient
load_dotenv(find_dotenv())

password=os.environ.get("MONGODB_PWD")

printer=pprint.PrettyPrinter()

#dbusername-aasvakoodalarasan & password- is in .env file
connectionstring=f"mongodb+srv://aasvakoodalarasan:{password}@cluster2.4hvpznb.mongodb.net/?retryWrites=true&w=majority"

client=MongoClient(connectionstring)

productvar=client.production

# https://www.youtube.com/watch?v=nYNAH8K_UhI
# https://mongo-arrow.readthedocs.io/en/latest/quickstart.html

#pymongoarrow is used to read data as pandas dataframe or as numpy array or as arrow table

#2)using pymongoarrow,read datas as arrow table 
patch_all()
author= Schema({"_id":ObjectId, "first_name":pyarrow.string(),"last_name":pyarrow.string(),"date_of_birth":dt})

arrow_table=productvar.author.find_arrow_all({},schema=author)
print(arrow_table)

#nope it didn't work
