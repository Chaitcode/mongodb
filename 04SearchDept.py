from pymongo import MongoClient

client=MongoClient("mongodb+srv://ChaitMango:<OffG09f4on>@emilyb.mgwlx.mongodb.net/office?retryWrites=true&w=majority")
db=client["office"]
coll=db["workers"]

dept=input("enter the department :")
dic={}
dic["department"]=dept
print(dic)

for doc in coll.find(dic):
    print(doc)
