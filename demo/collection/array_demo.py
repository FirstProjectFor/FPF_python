import array

s = b'd_+asdasdasd312'

arr = array.array('b', s)
print(arr)

arr = array.array('i', [1, 2, 3])
arr.extend([4, 5, 6])
arr.append(7)

print(arr)

"""
二维数组
"""

arr = [[0] * 5 for i in range(5)]
arr[0][0] = 1
print(arr)
