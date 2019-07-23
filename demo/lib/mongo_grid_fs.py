import gridfs
from pymongo import MongoClient

mongo_cli = MongoClient(host='192.168.0.201', port=27017)

test_db = mongo_cli['grid_fs_file']


def test_grid_fs():
    gf = gridfs.GridFS(test_db)
    gf.put('Hello MongoDB!', filename='test.txt', encoding='utf-8')
    file_list = gf.list()
    [print(file) for file in file_list]
    test_file_list = gf.find({'filename': 'test.txt'})
    [print('_id: {}, filename: {}'.format(file._id, file.filename)) for file in test_file_list]


test_grid_fs()
