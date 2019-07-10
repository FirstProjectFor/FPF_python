from __future__ import annotations

from util.file import file_replace_util
from util.file import files
from util.file.file_filter import JavaProjectFilter

replace_path = 'D:\\work\\cashloan\\dmc'
replace_file = '.\\replace.txt'

file_list = files.get_files_from_path(replace_path, JavaProjectFilter())

for file in file_list:
    replace_context = file_replace_util.package_replace(file, replace_file)
    print(replace_context)
    # file_replace.write_to_file(file, replace_context)
