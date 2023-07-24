import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]


#print(myclient.list_database_names())

mycol = mydb["order"]

mylist=[{"cust_name":"Ajay","item":"Bread","item_count":"2"},
        {"cust_name":"Nikhil","item":"Butter","item_count":"1"},
        {"cust_name":"Alisha","item":"Coke","item_count":"5"}
        ]


x=mycol.insert_many(mylist)