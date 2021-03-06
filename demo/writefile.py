def writefile(file_path, text):
    """
    把文本内容写入到文件里面
    :param file_path: 文件路径 \n
    :param text:文本内容 \n
    :return:
    """
    try:
        with open(file_path, mode="w", encoding="utf-8") as out:
            print(text, file=out)
    except IOError as err:
        print("向文件写入数据失败!" + str(err))
