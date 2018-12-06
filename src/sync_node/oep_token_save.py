import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["ont"]
mycol = mydb["oep_token"]

mylist = [
    {"contractAddress": "1ddbb682743e9d9e2b71ff419e97a9358c5c4ee9", "name": "DXToken" , "symbol":"DX"}
]

x = mycol.insert_many(mylist)

# 输出插入的所有文档对应的 _id 值
print(x.inserted_ids)