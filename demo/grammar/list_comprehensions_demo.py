names = ['zhangsan', 'lisi', 'wangwu', 'lisi']

# 列表转换
upper_name = [name.upper() for name in names]
print(upper_name)

# 过滤
filter_upper_name = [name.upper() for name in names if name != 'lisi']
print(filter_upper_name)

# 生成 generate
name_generate = (name for name in names)
[print(n) for n in name_generate]

# 转换成集合
set_names = {n for n in names}
print(type(set_names))
print(set_names)

# 转换字典
dict_names = {n: len(n) for n in names}
print(dict_names)
