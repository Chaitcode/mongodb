from pymongo import MongoClient

client=MongoClient("mongodb+srv://ChaitMango:<OffG09f4on>@emilyb.mgwlx.mongodb.net/office?retryWrites=true&w=majority")
db=client["office"]
coll=db["workers"]

lst=[]
for doc in coll.find():
    lst.append(doc)
    print(lst)