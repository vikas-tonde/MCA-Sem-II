import pymongo
mystudent = pymongo.MongoClient('localhost', 27017)
mydb = mystudent["zibacar"]
mycol = mydb["Student"]
for x in mycol.find():
    print(x)