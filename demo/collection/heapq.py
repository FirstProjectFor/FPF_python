import heapq
import random

random.seed(37)
data = []
for index in range(4):
    new_data = list(random.sample(range(1, 101), 5))
    new_data.sort()
    data.append(new_data)

for index, arr in enumerate(data):
    print('index:[{}], arr: {}'.format(index, arr))

# 不耗内存
for value in heapq.merge(*data):
    print(value)
