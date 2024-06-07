from dotenv import load_dotenv, find_dotenv
from datetime import datetime as dt
import os
import pprint

from pymongo import MongoClient
load_dotenv(find_dotenv())

password=os.environ.get("MONGODB_PWD")

printer=pprint.PrettyPrinter()

#dbusername-aasvakoodalarasan & password- is in .env file
connectionstring=f"mongodb+srv://aasvakoodalarasan:{password}@cluster2.4hvpznb.mongodb.net/?retryWrites=true&w=majority"

client=MongoClient(connectionstring)

productvar=client.production

#Using Advanced Queries of MongoDB
# https://www.youtube.com/watch?v=nYNAH8K_UhI

# https://www.mongodb.com/docs/manual/reference/operator/query/
# https://www.mongodb.com/docs/manual/reference/operator/aggregation/lookup/#-lookup--aggregation-

#1)Finding out book title which contains letter 'a' 
#books_containing_a=productvar.book.find({"title":{"$regex":"a{1}"}})
#printer.pprint(list(books_containing_a))
#########################################################################



#2)using lookup aggregation took(getting) datas by joining according to given inputs in it.joining means just for showcase, not realtime joining of database values
"""authors_and_books=productvar.author.aggregate([
        
    {
        "$lookup":
        {
            "from":"book",               #book is collection(table)
            "localField":"_id",          #_id is one of the field of book collection(table)
            "foreignField":"authors",    # authors is name of field assigning, not data of author collection(table)
            "as":"books"                 # books is also name of field assigning, not data of book collection(table)
        }
    }            
        
        #from book collection(table), taking _id and their corresponding datas and to put in the name of field as   "authors" under the name of "books" with author collection(table) in it.
    ])
printer.pprint(list(authors_and_books))
"""
######################################################################################################################




#3)adding an Field(just for showcase not in realtime database) by using $addField and to show it by using $project
authors_book_count=productvar.author.aggregate([
        
    {
        "$lookup":
        {
            "from":"book",               
            "localField":"_id",          
            "foreignField":"authors",    
            "as":"books"                 
        }
    }, 
    {
        "$addFields":
        {
        "total_books":{"$size":"$books"}
        }
    },
    {
        "$project":{"first_name":1,"last_name":1,"total_books":1,"_id":0},
    }          
        
        
    ])
printer.pprint(list(authors_book_count))

######################################################################################################################

#4)Showing Book written between at age of 20 to 23 by using some set of operators:
books_with_old_authors=productvar.book.aggregate([
        
    {
       "$lookup":
        {
            "from":"author",           # author is collection(table)
            "localField":"authors",    # authors is one of the field of book collection(table)  
            "foreignField":"_id",      # _id is name of field assigning, not original field of book collection(table)
            "as":"authors"             # authors is also name of field assigning, not data of author collection(table)
        }
    },
    {
        "$set":{
            "authors":{
                "$map":{
                    "input":"$authors",
                    "in":{
                        "age":{
                            "$dateDiff":{
                                "startDate":"$$this.date_of_birth",
                                "endDate":"$$NOW",
                                "unit":"year"
                            }
                        },
                        "first_name":"$$this.first_name",
                        "last_name":"$$this.last_name",
                        }
                    }
                }
            }
        },

        {
            "$match":{
                "$and":[
                    {"authors.age":{"$gte":20}},
                    {"authors.age":{"$lte":23}},
                ]
            }
        },
        {
            "$sort":{
                "age":1
            }
        }

    
    ])

printer.pprint(list(books_with_old_authors))

#######################################################################################################