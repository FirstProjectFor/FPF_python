import pickle

from util import printutil

movies = ["老无所依", 1954,
          "藩篱", 1955,
          "岁月神偷", 1966,
          "盗梦空间", 1983]

filename = "../data.txt"

try:
    with open(filename, mode="wb") as out:
        # 保存对象数据到文件
        pickle.dump(movies, file=out)
    with open(filename, mode="rb") as out:
        # 从文件中读取对象
        movies_copy = pickle.load(out)
        printutil.print_key_value("movies_copy is list", str(isinstance(movies_copy, list)))
except IOError as err:
    printutil.print_key_value("IOError", str(err))
except pickle.PickleError as p_err:
    printutil.print_key_value("PickleError", str(p_err))
