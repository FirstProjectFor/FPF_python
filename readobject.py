import pickle

movies = ["老无所依", 1954,
          "藩篱", 1955,
          "岁月神偷", 1966,
          "盗梦空间", 1983]

file = "data.txt"

try:
    with open("data.txt", mode="wb") as out:
        # 保存对象数据到文件
        pickle.dump(movies, file=out)

    with open("data.txt", mode="rb") as out:
        # 从文件中读取对象
        movies_copy = pickle.load(out)
        print(movies_copy)
        print("movies_copy is list: " + str(isinstance(movies_copy, list)))
except IOError as err:
    print(str(err))
except pickle.PickleError as p_err:
    print(str(p_err))
