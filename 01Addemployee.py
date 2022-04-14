from pymongo import MongoClient

id=int(input("enter id number :"))
nm=input("enter workers name: ")
age=int(input("enter age of worker :"))
dept=input("enter the department :")
post=input("enter the post :")
ct=input("enter the city :")
mb=int(input("enter mobile number :"))
sal=float(input("enter the salary :"))

dic={}
dic["_id"]=id
dic["name"]=nm
dic["age"]=age
dic["department"]=dept
dic["post"]=post
dic["city"]=ct
dic["mobile"]=mb
dic["salary"]=sal

client=MongoClient("mongodb+srv://ChaitMango:<OffG09f4on>@emilyb.mgwlx.mongodb.net/office?retryWrites=true&w=majority ")
db=client["office"]
coll=db["workers"]

coll.insert_one(dic)
print("New employee added to the Mongodb Atlas collection")