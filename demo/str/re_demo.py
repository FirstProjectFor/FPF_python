import re

# pattern = re.compile('(?P<g1>\d+)')

pattern = re.compile('''
                    # group name
                    (?P<g1>
                    # number
                    \d+
                    )''', re.VERBOSE)

text = '''
        At the end of some number of swaps, 
        A and B are both strictly increasing.  
        (A sequence is strictly increasing if and 
        only if A[0] < A[1] < A[2] < ... < A[A.length - 1].)
'''

for m in re.findall(pattern, text):
    print(m)

print()
match_ire = iter(re.finditer(pattern, text))
for m1 in match_ire:
    print(m1.groupdict())
