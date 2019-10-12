import ast

# 绝对值
print(abs(-1))
# 二进制
print(bin(-1))
print(bin(0))
print(bin(1))
print(format(10, 'b'))
print(format(-10, '#b'))

# any all
print(all([1, 1]))
print(any([0, 1]))
print(any([0, 0]))

# dir 不传参数输出当前作用域的模块和方法，传参数输出参数拥有的方法
print(dir({}))

for index, value in enumerate(range(2)):
    print(str(index) + ':' + str(value))
