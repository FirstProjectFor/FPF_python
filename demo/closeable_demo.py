from contextlib import contextmanager


# 可以用于 with 语句
@contextmanager
def custom_open(filename):
    f = open(filename)
    try:
        # 需要的时候打开
        # yield is a keyword that is used like return, except the function will return a generator.
        yield f
    finally:
        f.close()


with custom_open("data.txt") as f:
    print(f.read())


class Closeable(object):
    # 初始化
    def __init__(self, filename):
        print("init ...")
        self.file = open(filename)

    # as的时候赋值
    def __enter__(self):
        print("enter ...")
        return self.file

    # with执行结束之后调用
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("close...")
        self.file.close()


with Closeable("data.txt") as f:
    print(f.read())
