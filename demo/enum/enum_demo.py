import enum


@enum.unique  # 唯一值注释
class Status(enum.Enum):
    available = 1
    disable = 0


print(Status.available.value)

for status in Status:
    print('key:{:<10}, value:{:<10}'.format(status.name, status.value))

available = Status.available
print(Status.available is available)
print(Status.available == available)

# 新建枚举对象初始化枚举
BugStatus = enum.Enum(value='BugStatus', names={'fix_release': 1, 'fix_committed': 2})
for status in BugStatus:
    print('key:{:<15}, value:{:<15}'.format(status.name, status.value))


# 元组定义
class Foods(enum.Enum):
    fruit = (7, ['apple', 'lemon', 'watermelon'])
    meat = (8, ['pork', 'mutton', 'beef'])

    def __init__(self, code: int, species: list = ()):
        self.code = code
        self.species = species

    def contains(self, specie) -> bool:
        return specie in self.species


for food in Foods:
    print('key:{:<15}, value:{:<15}'.format(food.code, str(food.species)))


# 字典
class Foods_1(enum.Enum):
    food = {'code': 9, 'species': ['rice', 'wheat', 'peanut']}

    def __init__(self, val):
        self.code = val['code']
        self.species = val['species']


for food1 in Foods_1:
    print('key:{:<15}, value:{:<15}'.format(food1.code, str(food1.species)))
