def replace_controller_stream(file):
    '''
    Controller 替换工具
    1. `RequestMapping` 上面加一行 `@ResponseBody`
    2. `return void` 替换为Object
    3. `ServletUtils.writeToResponse(response, reposedata)` 替换为 `return reposedata`;
    4. 如果添加注解，导入类
    '''
    new_lines = []
    lines = reversed(read_lines(file))
    step = 0
    need_add_import = False
    has_add_import = False
    for line in lines:
        if step == 0 and 'ServletUtils.writeToResponse' in line and '//' not in line:
            start = int(line.index(','))
            end = int(line.index(')'))
            blank_len = int(len(line) - len(line.lstrip()))
            blank = line[0: blank_len]
            line = 'return ' + line[start + 1:end].strip() + ';\n'
            new_lines.append(blank + line)
            step = step + 1
        elif step == 1 and 'void' in line:
            line = line.replace('void', 'Object')
            new_lines.append(line)
            step = step + 1
        elif step == 2 and 'RequestMapping' in line:
            need_add_import = True
            new_lines.append(line)
            new_lines.append('    @ResponseBody' + '\n')
            step = 0
        elif step == 0 and 'import ' in line and need_add_import and not has_add_import:
            new_lines.append('import org.springframework.web.bind.annotation.ResponseBody;\n')
            new_lines.append(line)
            has_add_import = True
        else:
            new_lines.append(line)
    new_lines = reversed(new_lines)

    result = ''
    for line in new_lines:
        result = result + line

    return result


def package_replace(file, replace_file):
    replace_content = read_replace_context(replace_file)
    lines = read_lines(file)
    result = ''
    for line in lines:
        for key, value in replace_content.items():
            result = result + line.replace(key, value)
    return result


def read_replace_context(replace_file):
    replace_context = {}
    try:
        with open(replace_file, 'r') as file:
            for line in file.readlines():
                if line and len(line.strip().split(" ")) == 2:
                    key_value = line.strip().split(' ')
                    replace_context[key_value[0].strip()] = key_value[1].strip()
    except IOError as e:
        print(e)
    return replace_context


def write_to_file(file, context):
    try:
        with open(file, 'w', encoding='utf-8') as temp:
            temp.write(context)
    except IOError as e:
        print(e)


def read_lines(file):
    try:
        result = []
        with open(file, 'r', encoding='utf-8') as temp:
            for line in temp.readlines():
                result.append(line)
        return result
    except IOError as e:
        print(e)
