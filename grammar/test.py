#!/usr/bin/python3

import keyword
import sys


# print info in console
print("Hello World!")

# print keyword
print("\n\n\n\nKeyWord")
print(keyword.kwlist)

# 
if True:
   print(True)
else:
   print(False)

# 
input("\n\nPress Enter to continue!")
print("Total:")
total = (1 + 2 + 3 +
        4 + 5)
print(total)

# use sys
sys.stdout.write("Total:\t total\n")

# data type
counter = 100 # int
miles = 100.0 # float
name = "sunfeilong" # string

# stand data type
# Number : int float bool complex
# String : 
# List
# Tuple
# Sets
# Dictionary


# print type
a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d)) 

# extends

class A:
    pass

class B(A):
    pass

print(isinstance(A(), A))
print(type(A()) == A)
print(isinstance(B(), A))
print(type(B()) == A)

# delete 

del a

# error a is not define
# print(a)

print("\n\n\n")
print(3 + 7)
print(3 - 7)
print(3 * 7)
print(3 / 7)
print(3 // 7)
print(3 ** 7)









