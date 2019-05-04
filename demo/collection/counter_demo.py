import collections

"""
继承自 dict，值代表出现次数，可以用来表示优先级
"""

age_counter_arr = collections.Counter([1, 2, 3, 3])
print(age_counter_arr)
age_counter_tuple = collections.Counter(('1', '2', '3', '3'))
print(age_counter_tuple)
age_counter_dict = collections.Counter({'3': 2, '1': 1, '2': 1})
print(age_counter_dict)

age_counter_key_value = collections.Counter(a=2, b=3, c=4, e=1)

print('before change: ')
for e, number in age_counter_key_value.items():
    print(e, number)

# delete min counter elements
age_counter_key_value.pop('e')
# add element
age_counter_key_value['f'] = 3
# 增加统计次数，不是替换
age_counter_key_value.update(a=100)
age_counter_key_value.update(age_counter_arr)
age_counter_key_value.update({'c': 100, 'd': 200})
age_counter_key_value.update({'g': -100})
age_counter_key_value.elements()

print('after change: ')
for e, number in age_counter_key_value.items():
    print(e, number)

# 分数最高的前几个元素
print(age_counter_key_value.most_common(10))
# 按添加顺序显示元素
print(list(age_counter_key_value.elements()))

a = collections.Counter(a=3)
b = collections.Counter(a=2)
# & 取最大 | 取最小
print(a | b)
print(b & a)
