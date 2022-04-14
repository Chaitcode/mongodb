from pymongo import MongoClient

client=MongoClient("mongodb+srv://ChaitMango:<OffG09f4on>@emilyb.mgwlx.mongodb.net/office?retryWrites=true&w=majority")
db=client["office"]
coll=db["workers"]

sal=input("enter the salary :")
dic={}
dic["salary"]=sal
print(dic)

gsal={sal:{"$gt:value"}}

for doc in coll.find(gsal):
    print(doc)