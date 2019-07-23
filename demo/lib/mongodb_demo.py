import faker
import pymongo
from pymongo import MongoClient

faker = faker.Faker('ZH_CN')
mongo_cli = MongoClient(host='192.168.0.201', port=27017)

test_db = mongo_cli['test']


def base_test():
    user_collection = test_db['user']
    print('database info: {}'.format(test_db))
    print()
    print('collection info: {}'.format(user_collection))
    print()
    print('document count:{}'.format(user_collection.count_documents({})))
    print()
    id = None
    for user in user_collection.find({}):
        id = user['_id']
        print('user info: id: {:30} name:{:10} age:{:10}'.format(str(user['_id']), user['name'], user['age']))

    users = user_collection.find({'name': 'heihei'})
    for user in users:
        print(
            'user who name is \'heihei\': id: {:} name:{:20} age:{:10}'.format(user['_id'], user['name'], user['age']))
    print()

    young_user = user_collection.find({'age': {'$lte': 18}})
    for u in young_user:
        print('user who age is less than and eq 18: {}'.format(u))
    print()

    index_list = user_collection.list_indexes()
    for index in index_list:
        print('index: {:}'.format(index))
    print()

    # create ondex
    user_collection.create_index([('name', pymongo.ASCENDING)])

    admin_db = mongo_cli['admin']
    system_version_collection = admin_db['system.version']


def init_collection_data():
    person_collection = test_db['person']

    persons = []
    for num in range(1000000):
        if num > 0 and num % 10000 == 0:
            person_collection.insert_many(persons)
            persons.clear()
            print(person_collection.count_documents({}))
        persons.append({
            'name': faker.name(),
            'address': faker.address(),
            'phone': faker.phone_number(),
            'postcode': faker.postcode(),
            'age': str(faker.date_of_birth(minimum_age=18, maximum_age=30)),
            'company': faker.company(),
            'license_plate': faker.license_plate()
        })

    if persons:
        person_collection.insert_many(persons)


def update():
    update_collection = test_db['update_collection']
    # 删除数据
    update_collection.delete_many({})

    update_collection.insert_one({'_id': 123, 'name': 'LiLei'})
    # update_collection.insert_one({'_id': 123, 'name': 'LiLei'})
    update_collection.update_one({'name': 'LiLei'}, {'$inc': {'age': 3}}, upsert=True)
    update_collection.update_one({'name': 'LiLei'}, {'$addToSet': {'friends': 'Han MeiMei'}}, upsert=True)
    update_collection.update_one({'name': 'LiLei'}, {'$addToSet': {'friends': 'Han MeiMei'}}, upsert=True)
    update_collection.update_one({'name': 'LiLei'}, {'$addToSet': {'friends': 'Mr Wang'}}, upsert=True)
    update_collection.update_one({'name': 'LiLei'}, {'$push': {'friends': 'Mr Wang'}}, upsert=True)
    # 删除数组里面全部对应的元素
    # update_collection.update_one({'name': 'LiLei'}, {'$pull': {'friends': 'Mr Wang'}}, upsert=True)
    # 从数组尾部取出
    # update_collection.update_one({'name': 'LiLei'}, {'$pop': {'friends': 1}}, upsert=True)
    # 从数组头部取出
    # update_collection.update_one({'name': 'LiLei'}, {'$pop': {'friends': -1}}, upsert=True)
    # update_collection.update_one({'name': 'LiLei'}, {'$each': {'$addToSet': {'friends': 'Mr Wang'}}}, upsert=True)
    li_lei = update_collection.find_one({'name': 'LiLei'})
    print(li_lei)
    update_collection.update_one({'name': 'LiLei'}, {'$set': {'age': 4}}, upsert=True)
    # update_collection.update_one({'name': 'LiLei'}, {'$unset': {'age': True}}, upsert=True)
    li_lei = update_collection.find_one({'name': 'LiLei'})
    print(li_lei)


def test_find():
    find_collection = test_db['find_collection']
    find_collection.delete_many({})

    find_collection.insert_one({'name': 'zhangsan', 'age': 20})
    find_collection.insert_one({'name': 'li si', 'age': 20})
    find_collection.insert_one({'name': 'wang wu', 'age': 21})
    find_collection.insert_one({'name': 'zhou liu', 'age': 22})

    # 只返回 age 字段
    zhangsan = find_collection.find_one({'name': 'zhangsan'}, {'age': 1})
    print(zhangsan)
    persons = find_collection.find({'age': {'$in': [20, 21]}})
    # persons = find_collection.find({'age': {'$nin': [22]}})
    [print(p) for p in persons]
    persons = find_collection.find({'$or': [{'name': {'$eq': 'zhangsan'}}, {'age': {'$in': [22]}}]})
    [print(p) for p in persons]


def test_index():
    test_db.drop_collection('index_collection')
    index_collection = test_db['index_collection']
    index_collection.insert_one({'name': 'xiaotian', 'age': 20})
    index_collection.create_index([('name', 1), ('age', 1)])
    index_collection.create_index([('name', 1), ('age', 1)])
    [print(index) for index in index_collection.list_indexes()]


def test_geo():
    geo_collection = test_db['geo_collection']
    geo_collection.delete_many({})
    geo_collection.insert_one({'name': 'beijing', 'gps': (10, 20)})
    geo_collection.insert_one({'name': 'beijing', 'gps': (0, 10)})
    geo_collection.insert_one({'name': 'beijing', 'gps': (0, -10)})
    geo_collection.insert_one({'name': 'beijing', 'gps': (10, 0)})
    geo_collection.insert_one({'name': 'beijing', 'gps': (-10, 0)})
    geo_collection.insert_one({'name': 'beijing', 'gps': (30, 30)})
    geo_collection.insert_one({'name': 'beijing', 'gps': (40, 40)})

    geo_collection.create_index([('gps', '2d')])

    print('near:')
    points = geo_collection.find({'gps': {'$near': (0, 0)}}).limit(3)
    [print(p) for p in points]
    print('in box:')
    points = geo_collection.find({'gps': {'$within': {'$box': [[0, 0], [30, 30]]}}}).limit(10)
    [print(p) for p in points]


# base_test()
# init_collection_data()
# update()
# test_find()
# test_index()

test_geo()
