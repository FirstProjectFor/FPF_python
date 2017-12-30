import sys


def list_arr(array=[], indent=False, level=0, out=sys.stdout):
    """
    把数据里面的数据格式化输出到指定输出\n
    :param array:  数组\n
    :param indent: 是否输出层级格式化空格\n
    :param level:  数组等级\n
    :param out:    输出，默认为标准输出\n
    :return:
    """
    if isinstance(array, list):
        for a in array:
            list_arr(a, indent, level + 1, out)
    else:
        if indent:
            for l in range(level):
                print("\t", end="", file=out)
        print(array, file=out)
    return
