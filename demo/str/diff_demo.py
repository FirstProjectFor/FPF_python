import difflib

text1 = '''
Welcome to China.
My name is XiaoTian.
Where are you from ?
'''

text2 = '''
Welcome to China.
My name is Xiao.
'''

d = difflib.Differ()

diff_info = d.compare(text1.splitlines(), text2.splitlines())
print("\n".join(diff_info))
print()
print()
print()

diff_info = difflib.unified_diff(text1.splitlines(), text2.splitlines())
print("\n".join(diff_info))
