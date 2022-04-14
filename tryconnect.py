from pymongo import MongoClient

try:
    client=MongoClient("mongodb+srv://ChaitMango:<OffG09f4on>@emilyb.mgwlx.mongodb.net/office?retryWrites=true&w=majority")
    db=client["office"]
    print("connected sucessfully")
except:
    print("connection failed")    