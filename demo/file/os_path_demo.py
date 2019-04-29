import os
import time

file1 = "d://test.pdf"
file2 = "d://tmp//"

print(os.path.isabs(file1))
print(os.path.isdir(file2))

print("split ---")
print(os.path.split(file1))
print(os.path.splitext(file1))

print(os.path.split(file2))
print(os.path.splitext(file2))

print(os.path.basename(file1))
print(os.path.dirname(file1))

print(os.path.abspath(file1))

print(time.ctime(os.path.getctime(file1)))
print(os.path.getsize(file1))
print(os.path.getsize(file2))


