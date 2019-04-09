import gridfs
import pymongo
from pymongo import InsertOne, UpdateMany, UpdateOne, DeleteOne, DeleteMany, ReplaceOne, IndexModel


def init_db(cl, database="tests"):
    return cl.get_database(database)


def auth(db, username, password):
    db.authenticate(name=username, password=password)


def delete_data(db):
    # 删除数据
    d_result = db.get_collection("inventory").delete_many({})
    d_result = db.get_collection("stores").delete_many({})
    print(d_result.deleted_count)


def insert_data(db):
    # 删除数据
    delete_data(db)
    # 插入多个，集合不存在会自动创建
    db.inventory.insert_many([
        {"item": "journal", "qty": 25, "status": "A",
         "size": {"h": 14, "w": 21, "uom": "cm"}, "tags": ["blank", "red"]},
        {"item": "notebook", "qty": 50, "status": "A",
         "size": {"h": 8.5, "w": 11, "uom": "in"}, "tags": ["red", "blank"]},
        {"item": "paper", "qty": 100, "status": "D",
         "size": {"h": 8.5, "w": 11, "uom": "in"}, "tags": ["red", "blank", "plain"]},
        {"item": "planner", "qty": 75, "status": "D",
         "size": {"h": 22.85, "w": 30, "uom": "cm"}, "tags": ["blank", "red"]},
        {"item": "postcard", "qty": 45, "status": "A",
         "size": {"h": 10, "w": 15.25, "uom": "cm"}, "tags": ["blue"]}
    ])
    db.inventory.insert_many([
        {"item": "journal", "qty": 25, "tags": ["blank", "red"], "dim_cm": [14, 21]},
        {"item": "notebook", "qty": 50, "tags": ["red", "blank"], "dim_cm": [14, 21]},
        {"item": "paper", "qty": 100, "tags": ["red", "blank", "plain"], "dim_cm": [14, 21]},
        {"item": "planner", "qty": 75, "tags": ["blank", "red"], "dim_cm": [22.85, 30]},
        {"item": "postcard", "qty": 45, "tags": ["blue"], "dim_cm": [10, 15.25]}
    ])
    db.inventory.insert([{"item": None}, {}])
    db.get_collection("stores").insert_many(
        [
            {"name": "Java Hut", "description": "Coffee and cakes"},
            {"name": "Burger Buns", "description": "Gourmet hamburgers"},
            {"name": "Coffee Shop", "description": "Just coffee"},
            {"name": "Clothes Clothes Clothes", "description": "Discount clothing"},
            {"name": "Java Shopping", "description": "Indonesian goods"}
        ]
    )
    # 文本字段创建索引用于搜索，一个集合只允许创建一个文本索引，可以是多个字段
    index = IndexModel([("name", pymongo.TEXT), ("description", pymongo.TEXT)], name="name_description")
    db.get_collection("stores").create_indexes([index])


def update_date(db):
    db.get_collection("inventory").update_many(
        {"item": "paper"},
        {"$set": {"size.uom": "cm", "status": "P"}, "$currentDate": {"lastModified": True}},
        upsert=True
    )

    db.get_collection("inventory").replace_one(
        {"item": "paper"},
        {"item": "paper", "instock": [{"warehouse": "A", "qty": 60}, {"warehouse": "B", "qty": 40}]}
    )


def search_date(db):
    # 查询数据
    for name in db.collection_names():
        collection = db.get_collection(name)
        for doc in collection.find().limit(10000).skip(0):
            print(doc)

    result = db.get_collection("inventory").find({"$or": [{"status": "D"}, {"qty": 75}]})
    result = db.get_collection("inventory").find({"$or": [{"status": "D"}, {"status": "A"}]})
    result = db.get_collection("inventory").find({"$and": [{"status": "D"}, {"qty": 75}]})
    result = db.get_collection("inventory").find({"status": "D", "qty": 75})
    result = db.get_collection("inventory").find({"size": {"h": 14, "w": 21, "uom": "cm"}})
    result = db.get_collection("inventory").find({"size": {"h": 14, "w": 21, "uom": "cm"}})
    result = db.get_collection("inventory").find({"tags": ["blank", "red"]})
    result = db.get_collection("inventory").find({"tags": {"$all": ["red", "blank"]}})
    result = db.get_collection("inventory").find({"status": {"$in": ["A", "D"]}})
    result = db.get_collection("inventory").find({"dim_cm": {"$gt": 25}})
    result = db.get_collection("inventory").find({"dim_cm": {"$gt": 15, "$lt": 20}})
    result = db.get_collection("inventory").find({"dim_cm": {"$elemMatch": {"$gt": 22, "$lt": 30}}})
    result = db.get_collection("inventory").find({"dim_cm.1": {"$gt": 25}})
    result = db.get_collection("inventory").find({"tags": {"$size": 3}})

    result = db.get_collection("inventory").find(
        {"status": "A", "$or": [{"qty": {"$lt": 30}}, {"item": {"$regex": "^p"}}]})

    result = db.get_collection("inventory").find({"status": "D", "qty": 75}, {"item": 1, "status": 1})
    result = db.get_collection("inventory").find({"status": "D"}, {"item": 1, "size.h": 1, "tags": {"$slice": 2}})
    result = db.get_collection("inventory").find({"item": None})
    result = db.get_collection("inventory").find({"item": {"$type": 10}})
    result = db.get_collection("inventory").find({"item": {"$exists": False}})

    result = db.get_collection("stores").find({"$text": {"$search": "java coffee shop"}})
    # coffee shop 短语
    result = db.get_collection("stores").find({"$text": {"$search": "java \"coffee shop\""}})
    # 排除单词
    result = db.get_collection("stores").find({"$text": {"$search": "java -coffee shop"}})
    # 相关性评分
    result = db.get_collection("stores").find(
        {"$text": {"$search": "java coffee shop"}},
        {"score": {"$meta": "textScore"}}
    ).sort([("score", {"$meta": "textScore"})])

    print("search: -------------------------------------------------")
    for document in result:
        print(document)


def save_file(db):
    # 存储文件
    gfs = gridfs.GridFS(db)
    with open("data.txt", mode="r", encoding="utf-8") as in_file:
        if gfs.exists(document_or_id="1"):
            gfs.delete(file_id="1")
        file_id = gfs.put(in_file.read(), _id="1", filename="data.txt", encoding="utf-8")
        print(gfs.list())
        content = gfs.get(file_id).read()
        print(content)


def bulk(db):
    requests = list();
    requests.append(InsertOne({"name": "x", "age": 23}))
    requests.append(InsertOne({"name": "x", "age": 23}))
    requests.append(InsertOne({"name": "x", "age": 25}))
    requests.append(UpdateOne({"name": "x"}, {"$set": {"age": 25}}))
    requests.append(UpdateMany({"name": "x"}, {"$set": {"age": 24}}))
    requests.append(ReplaceOne({"name": "x"}, {"name": "x", "age": 23, "sex": "man"}))
    requests.append(DeleteOne({"name": "x"}))
    requests.append(DeleteMany({"name": "x"}))
    result = db.get_collection("tests").bulk_write(requests)
    print("bulk API", result.bulk_api_result, sep=" : ")


def geo_search(db):
    d.drop_collection("places")
    db.get_collection("places").insert({
        "name": "Central Park",
        "location": {
            "type": "Point",
            "coordinates": [-73.97, 40.77]
        },
        "category": "Parks"
    })
    db.get_collection("places").insert({
        "name": "Sara D. Roosevelt Park",
        "location": {
            "type": "Point",
            "coordinates": [-73.9928, 40.7193]
        },
        "category": "Parks"
    })
    db.get_collection("places").insert({
        "name": "Polo Grounds",
        "location": {
            "type": "Point",
            "coordinates": [-73.9375, 40.8303]
        },
        "category": "Stadiums"
    })
    # 创建索引
    index = IndexModel([("location", pymongo.GEOSPHERE)], name="location_2ds")
    db.get_collection("places").create_indexes([index])
    # 查询，在范围之间
    result = db.get_collection("places").find({
        "location": {
            "$near": {
                "$geometry": {"type": "Point", "coordinates": [-73.9667, 40.78]},
                "$minDistance": 1000,
                "$maxDistance": 5000
            }
        }
    })
    print("geo search ----------------------------------------------")
    for document in result:
        print(document)


client = pymongo.MongoClient("localhost", 27017)
d = init_db(client, "tests")
auth(d, "tests", "000000")
insert_data(d)
update_date(d)
search_date(d)
geo_search(d)
bulk(d)
client.close()
