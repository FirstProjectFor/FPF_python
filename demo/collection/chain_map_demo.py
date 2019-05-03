import collections

'''
联合多个字典
'''

dict_a = {'a': 'A', 'b': 'B'}
dict_b = {'c': 'D', 'b': 'b'}

m = collections.ChainMap(dict_a, dict_b)

# 按联合顺序查找
print(m['b'])
print('keys:{}'.format(list(m.keys())))
print('keys:{}'.format(list(m.values())))
print(m.maps)
m.maps = list(reversed(m.maps))
print(m.maps)
# 在以有映射列表前面创建一个映射
m_c = m.new_child()
# 增加和变更元素只会在第一个映射进行修改
m_c['d'] = 'D'
m_c['e'] = 'E'
m_c['a'] = 'a'
print(m_c.maps)
print(m.maps)
