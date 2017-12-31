from demo import readfile as rd


def testreadfile():
    filename = "../data.txt"
    lines = rd.readfile(filename)
    for line in lines:
        print(line)


testreadfile()
