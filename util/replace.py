import pathlib
import queue

replace_context = {}

replace_file = '.\\replace.txt'
replace_path = 'D:\\work\\asdads'


def replace(context: str):
    for key, value in replace_context.items():
        context = context.replace(key, value)
    return context


def not_replace(file_name):
    if str(file_name).endswith('pom.xml'):
        return True
    if str(file_name).endswith('.cmd'):
        return True
    if str(file_name).endswith('.iml'):
        return True
    if str(file_name).endswith('mvnw'):
        return True
    if str(file_name).endswith('.gitignore'):
        return True
    if str(file_name).endswith('.properties'):
        return True
    if str(file_name).endswith('.md'):
        return True
    if str(file_name).endswith('.xls'):
        return True
    if str(file_name).endswith('.js'):
        return True
    if str(file_name).endswith('.class'):
        return True
    if 'static' in str(file_name):
        return True
    return False


# read replace context
try:
    with open(replace_file, 'r') as file:
        for line in file.readlines():
            if line and len(line.strip().split(" ")) == 2:
                key_value = line.strip().split(' ')
                replace_context[key_value[0].strip()] = key_value[1].strip()
except IOError as e:
    print(e)

replace_path_queue = queue.Queue()
replace_path_queue.put(pathlib.Path(replace_path))

replace_file_queue = queue.Queue()

while replace_path_queue.qsize() > 0:
    path = replace_path_queue.get()
    for child in path.iterdir():
        if child.is_dir() and "dmc-" in str(child):
            replace_path_queue.put(child)
        elif child.is_file():
            if not_replace(child):
                print(child)
            else:
                replace_file_queue.put(child)
        else:
            pass

while replace_file_queue.qsize() > 0:
    replace_file = replace_file_queue.get()
    try:
        print(replace_file)
        text = ''
        with open(replace_file, 'r', encoding='utf-8') as temp1:
            for line in temp1.readlines():
                text = text + replace(line)
        with open(replace_file, 'w', encoding='utf-8') as temp2:
            temp2.write(text)
    except IOError as e:
        print(e)
