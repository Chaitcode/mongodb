from pymongo import MongoClient

client=MongoClient("mongodb+srv://ChaitMango:<OffG09f4on>@emilyb.mgwlx.mongodb.net/office?retryWrites=true&w=majority")
db=client["office"]
coll=db["workers"]

coll1=db["exworkers"]

id=int(input("enter the id :"))
qr={}
qr["_id"]=id
print(qr)

for doc in coll.find(qr):
    print(doc)

for doc in coll1:
    print(doc)

documentsToMove = db.coll.find({qr})
documentsToMove.forEach(function(qr)) 
db.coll1.insert(doc)
db.coll.remove(doc)
    




#Mcoll.delete_One(qr)
print("Document deleted from workers and moved to exworkers.....")

