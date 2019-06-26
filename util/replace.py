import pathlib
import queue

replace_context = {}

replace_file = '.\\replace.txt'
replace_path = 'D:\\replace'


def replace(context: str):
    for key, value in replace_context.items():
        context = context.replace(key, value)
    return context


# read replace context
try:
    with open(replace_file, 'r') as file:
        for line in file.readlines():
            if line and len(line.strip().split(",")) == 2:
                key_value = line.strip().split(' ')
                replace_context[key_value[0]] = key_value[1]
except IOError as e:
    print(e)

replace_path_queue = queue.Queue()
replace_path_queue.put(pathlib.Path(replace_path))

replace_file_queue = queue.Queue()

while replace_path_queue.qsize() > 0:
    path = replace_path_queue.get()
    for child in path.iterdir():
        if child.is_dir():
            replace_path_queue.put(child)
        elif child.is_file():
            replace_file_queue.put(child)
        else:
            pass

while replace_file_queue.qsize() > 0:
    replace_file = replace_file_queue.get()
    try:
        print(replace_file)
        text = ''
        with open(replace_file, 'r') as temp1:
            for line in temp1.readlines():
                text = text + replace(line)
        with open(replace_file, 'w') as temp2:
            temp2.write(text)
    except IOError as e:
        print(e)
