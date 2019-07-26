import random

print('random.randint() random generate a number from [1,3]: {}'.format(random.randint(1, 3)))
print('random.choice() random choice a element from seq. value: {}'.format(random.choice([1, 2, 3, 4, 5])))
print('random select \'k\' number from [1,2,3,4]: value {}'.format(random.choices([1, 2, 3, 4], k=5)))
print('random.random(), generate a float number in range [0.1.0)'.format(random.random()))
print('random.expovariate(lambd=x), generate a value random.rand()/lambd. value: {} '.format(
    random.expovariate(lambd=0.01)))
