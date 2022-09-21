# import MongoClient
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['zibacar']
print("Database is created !!")


from pymongo import MongoClient
myclient = MongoClient("mongodb://localhost:27017/")

db = myclient["zibacar"]

collection = db["Student"]
record = { "_id": 5,
		"name": "Raju",
		"Roll No": "1005",
		"Branch": "CSE"}
rec_id1 = collection.insert_one(record)


from pymongo import MongoClient
myclient = MongoClient("mongodb://localhost:27017/")
db = myclient["zibacar"]
collection = db["Student"]
mylist = [
{ "_id": 1, "name": "Vishwash", "Roll No": "1001", "Branch":"CSE"},
{ "_id": 2, "name": "Vishesh", "Roll No": "1002", "Branch":"IT"},
{ "_id": 3, "name": "Shivam", "Roll No": "1003", "Branch":"ME"},
{ "_id": 4, "name": "Yash", "Roll No": "1004", "Branch":"ECE"},
]
collection.insert_many(mylist)


import pymongo
mystudent = pymongo.MongoClient('localhost', 27017)
mydb = mystudent["zibacar"]
mycol = mydb["Student"]
for x in mycol.find():
    print(x)


# importing Mongoclient from pymongo
from pymongo import MongoClient


# Making Connection
myclient = MongoClient("mongodb://localhost:27017/")

# database
db = myclient["Singh"]

Collection = db["Student"]

cursor = Collection.find({"Marks":{"$gt":"45"}})


print("The data having Marks greater than 45 is:")
for record in cursor:
	print(record)

cursor = Collection.find({"Marks":{"$lt":"45"}})

print("\nThe data having Quantity less than 40 is:")
for record in cursor:
	print(record)
