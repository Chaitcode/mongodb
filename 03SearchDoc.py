from pymongo import MongoClient

client=MongoClient("mongodb+srv://ChaitMango:<OffG09f4on>@emilyb.mgwlx.mongodb.net/office?retryWrites=true&w=majority")
db=client["office"]
coll=db["workers"]

code=int(input("enter the id :"))
qr={}
qr["_id"]=code
print(qr)

for doc in coll.find_one(qr):
    print(doc)

