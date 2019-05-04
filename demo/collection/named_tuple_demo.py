import collections

Person = collections.namedtuple('Person', 'name age sex')

xiao_tian = Person(name='XiaoTian', age=24, sex='male')

print(xiao_tian)
print(xiao_tian.name)
print(xiao_tian._fields)
print(xiao_tian._asdict())
xiao_tian_replace = xiao_tian._replace(name='s')
print(xiao_tian_replace)
