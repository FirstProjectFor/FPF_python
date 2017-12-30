from xpinyin import Pinyin

p = Pinyin()
pinyin = p.get_pinyin("孙飞龙", splitter="", show_tone_marks=False, convert="lower")
first_char = p.get_initials("孙飞龙", splitter="").lower()
print(pinyin)
print(first_char)

name = "《Flask：一个使用Python编写的轻量级Web应用框架》"

pinyin = p.get_pinyin(name, splitter="")
first_char = p.get_initials(name, splitter="")

print(pinyin)
print(first_char)

