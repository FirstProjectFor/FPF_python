import gridfs
import pymongo
from pymongo import ReturnDocument

client = pymongo.MongoClient("localhost", 27017)

db = client.get_database("test")

# admin 在命令行添加用户
# db.createUser(
#   {
#     user: "test",
#     pwd: "000000",
#     roles: [
#        { role: "readWrite", db: "test" }
#     ]
#   }
# )

# 认证
db.authenticate(name="test", password="000000")

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

# 查询数据
for name in db.collection_names():
    collection = db.get_collection(name)
    for document in collection.find().limit(10000).skip(0):
        print(document)

# 存储文件
gfs = gridfs.GridFS(db)
with open("data.txt", mode="r", encoding="utf-8") as in_file:
    if gfs.exists(document_or_id="1"):
        gfs.delete(file_id="1")
    file_id = gfs.put(in_file.read(), _id="1", filename="data.txt", encoding="utf-8")
    print(gfs.list())
    content = gfs.get(file_id).read()
    print(content)

client.close()
