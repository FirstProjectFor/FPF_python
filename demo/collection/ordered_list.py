import bisect

arr = [1, 2, 4, 2, 1, 1, 2, 7, 6, 41, 2, 3, 4]
sort_arr = []

for number in arr:
    bisect.insort_right(sort_arr, number)

print(arr)
print(sort_arr)
