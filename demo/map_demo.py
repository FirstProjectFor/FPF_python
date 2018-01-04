import random


def exists(nums, target):
    """
    检查数组里面的元素,是否有两个的和等于目标值
    :param nums: 数组
    :param target: 目标值
    :return: 存在返回元素的下标，不存在返回 Fasle
    """
    t_map = dict()
    for index, val in enumerate(nums):
        if val in t_map:
            return [t_map[val], index]
        else:
            temp = target - val
            t_map[temp] = index
    return False


def test():
    numbers = list()
    target = 1000
    for i in range(target):
        n = random.randint(0, target)
        numbers.append(n)
        result = exists(numbers, target)
        if not result:
            print("not exists !")
        else:
            print(result)


test()
