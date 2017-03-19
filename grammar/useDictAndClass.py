#!/usr/bin/python3

# use Dict
my_dict = dict()
my_dict['name'] = 'my';
test_dict = {}
test_dict['name'] = 'test'
print(my_dict)
print(test_dict)

# use class
class Person:
    def __init__(self, p_name,p_age):
        self.name = p_name
        self.age = p_age
    # return age
    def getAge(self):
        return self.age
    # return name
    def getName(self):
        return self.name

# init Person
p = Person('sun','24')
print(p.name)
print(p.age)
print(str(p))

# change Name
p.name = 'fei'
print(p.name)
# print Person calss method
print(dir(p))

# extend
class PersonList(list):
    def __init__(self):
        # call parent class init method
        list.__init__([])


pl = PersonList()

print(dir(pl))


