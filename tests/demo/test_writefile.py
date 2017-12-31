from demo import readfile as rf
from demo import writefile as wf


def testwritefile():
    filename = "../data.txt"
    data = "我的名字是小田，欢迎使用Python"
    wf.writefile(filename, data)
    lines = rf.readfile(filename)
    for line in lines:
        print(line, end=" ")


testwritefile()
