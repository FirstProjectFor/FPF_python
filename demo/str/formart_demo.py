import math

sentence = 'My name is LiLie'
print(sentence.lower().count('n'))
print(len(sentence))
print(''.join([str.upper(v) for v in reversed(sentence)]))
print()

pi = math.pi
print(pi)
print('{}'.format('123\s'))
print('{!r}'.format('123\s'))
print(str('123\s'))
print(repr('123\s'))

print('*.****:{:<20.4f}'.format(pi))
print('*.****:{:<20.4f}'.format(pi * (10 ** 9)))
print('c:{:c}'.format(20))
print('b:{:b}'.format(20))
print('o:{:o}'.format(20))
print('d:{:d}'.format(20))
print('x:{:x}'.format(20))
print('e:{:e}'.format(20))
print('g:{:g}'.format(20))
