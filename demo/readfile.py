def readfile(file_path):
    """
    读取文件里面的内容并输出到控制台\n
    :param file_path:  文件路径 \n
    :return: void\n
    """
    try:
        with open(file_path, encoding="utf-8") as file_stream:
            for line in file_stream:
                try:
                    yield line
                except ValueError:
                    print(line, end="")
    except IOError as err:
        print("没有找到文件" + str(err))
