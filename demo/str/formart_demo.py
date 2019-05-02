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

print('{:<20.4f}'.format(pi))
print('{:<20.4f}'.format(pi * (10 ** 9)))
print('{:c}'.format(20))
print('{:b}'.format(20))
print('{:o}'.format(20))
print('{:d}'.format(20))
print('{:x}'.format(20))
print('{:e}'.format(20))
print('{:g}'.format(20))
print('{:s}'.format({'name': 'LiLei'}))
