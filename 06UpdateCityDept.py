from pymongo import MongoClient


id=int(input("enter the id :"))
qr={}
qr["_id"]=id
print(qr)

nct=input("enter the new city:")
nc={}
nc["city"]=nct
print(nc)

ndept=input("enter the new department:")
nd={}
nd["department"]=ndept
print(nd)


upd={"$set":(nc,nd)}

client=MongoClient("mongodb+srv://ChaitMango:<OffG09f4on>@emilyb.mgwlx.mongodb.net/office?retryWrites=true&w=majority")
db=client["office"]
coll=db["workers"]

coll.update_One(upd,qr)
print("Salary updated......")

for doc in coll.find():
    print(doc)