import pathlib


def traverse_path(path: pathlib.Path, level: int):
    """遍历文件"""
    try:
        if path:
            if path.is_dir():
                print_dir(path, level)
                for f in path.iterdir():
                    traverse_path(f, level + 1)
            elif path.is_file():
                print_file(path, level)
            else:
                pass
    except PermissionError as e:
        pass


def print_file(file: pathlib.Path, level: int):
    print_with_blank(file.name, "-", level)


def print_dir(directory: pathlib.Path, level: int):
    print_with_blank(str(directory), "+", level)


def print_with_blank(file_str: str, prefix: str, level: int):
    for n in range(level):
        print(" ", end="")
    print(prefix + " " + file_str)


file_path = pathlib.Path("C:\\Users\\sunfeilong\\Desktop\\name")
traverse_path(file_path, 0)

pure_path = pathlib.PurePath("c://")

print(pure_path / "name")
print(type(pure_path / "name"))
