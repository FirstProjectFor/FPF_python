import pathlib
import queue


def get_files_from_path(file_path, file_filter):
    replace_path_queue = queue.Queue()
    replace_path_queue.put(file_path)
    result = []

    while replace_path_queue.qsize() > 0:
        path = replace_path_queue.get()
        path = pathlib.Path(path)

        for child_file in path.iterdir():
            if child_file.is_dir():
                replace_path_queue.put(child_file)
            elif child_file.is_file():
                if (file_filter.filter(child_file)):
                    pass
                else:
                    result.append(child_file)
            else:
                pass
    return result
