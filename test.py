import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]


#print(myclient.list_database_names())

mycol = mydb["customers"]


#print(mydb.list_collection_names())


mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)