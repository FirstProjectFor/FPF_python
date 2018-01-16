import pymongo
from pymongo import ReturnDocument

client = pymongo.MongoClient("localhost", 27017)

db = client.get_database("test")

# 插入测试数据
if "test" in db.collection_names():
    db.drop_collection("test")

test_collection = db.create_collection("test")
for i in range(10):
    temp = dict()
    temp["number"] = i
    test_collection.insert_one(temp)

# 更新数据
for i in range(10):
    filter_temp = dict()
    filter_temp["number"] = i
    update_temp = dict()
    update_temp["$inc"] = dict()
    update_temp["$inc"]["number"] = -9
    test_collection.update_one(filter_temp, update_temp)

    filter_temp = {"number": i - 9}
    update_temp = {"$set": {"origin_number": i}}
    before = test_collection.find_one_and_update(filter_temp, update_temp, return_document=ReturnDocument.BEFORE)
    print(before)

#


# 查询数据
for name in db.collection_names():
    collection = db.get_collection(name)
    for document in collection.find().limit(10000).skip(0):
        print(document)
