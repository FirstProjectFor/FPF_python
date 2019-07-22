import pymongo
from pymongo import MongoClient

mongo_cli = MongoClient(host='192.168.0.201', port=27017)

test_db = mongo_cli['test']
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
    print('user who name is \'heihei\': id: {:} name:{:20} age:{:10}'.format(user['_id'], user['name'], user['age']))
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
