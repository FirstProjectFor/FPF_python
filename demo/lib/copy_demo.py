import copy

data = {
    'name': 'zhangsan',
    'age': 'lisi'
}
data_copy = copy.deepcopy(data)

print(data)
print(data_copy)
