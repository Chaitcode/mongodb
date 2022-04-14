from pymongo import MongoClient

id=int(input("enter the id :"))
qr={}
qr["_id"]=id
print(qr)

nsal=float(input("enter the new salary :"))
ns={}
ns["salary"]=nsal
print(ns)


upd={"$set":ns}

client=MongoClient("mongodb+srv://ChaitMango:<OffG09f4on>@emilyb.mgwlx.mongodb.net/office?retryWrites=true&w=majority")
db=client["office"]
coll=db["workers"]


coll.update_one(qr,upd)
print("Salary updated......")

for doc in coll.find():
    print(doc)


    #collection.find_one_and_update({"_id":"0"}, {"$set" : {"user_name" : updated_user_name}}, upsert = 0 )