#!/bin/python3

from util import print_array

movies = ["老无所依", "藩篱", "岁月神偷"]

print(len(movies))
# reverse
movies.reverse()
# append
movies.append("盗梦空间")
# copy
moviesCopy = movies.copy()
moviesCopy.append("当幸福来敲门")
# extend
moviesCopy.extend(movies)
# insert
moviesCopy.insert(1, "变形金刚")
# remove : remove first occurrence of value. Raises ValueError if the value is not present
moviesCopy.remove("变形金刚")

movies = ["老无所依", 1954,
          "藩篱", 1955,
          "岁月神偷", 1966,
          "盗梦空间", 1983]
# for
for movie in movies:
    print(movie)

# while
count = 0
while count < len(movies):
    print("《", movies[count], "》 :", movies[count + 1])
    count = count + 2

# arr
arr = [1, 2, 3, [4, 5, 6, [7, 8, 9]]]
print(arr[3][3][2] == 9)

# print list
print(arr)
with open("data.txt", "w") as out:
    print_array.list_arr(arr, indent=False, level=0, out=out)
    print()

# range
for number in range(4):
    print(number, end="")
print()

# iterator
moviesIterator = enumerate(movies, 0)
print(moviesIterator.__next__())
print(moviesIterator.__next__())

has_blank = " My name is XiaoTian "
has_blank = has_blank.strip()
print(has_blank)

# 字典
person = dict()
person["name"] = "XiaoTian"
print(person)
