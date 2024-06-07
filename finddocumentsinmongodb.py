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

printer=pprint.PrettyPrinter()    #It will used to print result in terminal

def finddocuments():

    records=person_collectionvar.find()

    for dbrecord in records:
        printer.pprint(dbrecord)

finddocuments()


def findparticulardocument():
    singlerecord=person_collectionvar.find_one({"first_name":"Tim"})
    printer.pprint(singlerecord)

findparticulardocument()


#get record by id
def  getbyid(person_id):
    from bson.objectid import ObjectId

    _id=ObjectId(person_id)
    recordbyid=person_collectionvar.find_one({"_id":_id})
    printer.pprint(recordbyid)

getbyid("64f6dabee89b4acfe8db6da0")


#get record between ranges
def getrecordbetweenranges(min_age,max_age):
    query={
        "$and":[
            
                {"age":{"$gte":min_age}},
                {"age":{"$lte":max_age}}
            ]}
    recordrange=person_collectionvar.find(query).sort("age")
    for rangedrecords in recordrange:
        printer.pprint(rangedrecords)

getrecordbetweenranges(20,35)


#get wanted fields only
def wantedfields():
    columns={"_id":0,"first_name":1,"last_name":1}

    # 0 means don't want that field and 1 means i want that field

    fieldofrecords=person_collectionvar.find({},columns)
    for recordswithneededfields in fieldofrecords:
        printer.pprint(recordswithneededfields)

wantedfields()


#Now Count No of documents(records) in it
def countrecords():
    count=person_collectionvar.count_documents(filter={})
    print("Number of Record is",count)

countrecords()