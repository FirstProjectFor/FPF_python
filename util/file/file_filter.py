import pathlib


class FileFilter:

    def name_filter(self, name):
        pass

    def filter(self, path: pathlib.Path):
        return self.name_filter(path.name)


class JavaProjectFilter(FileFilter):

    def name_filter(self, file_name):
        if file_name.endswith('.java') or file_name.endswith('Mapper.xml'):
            return False
        return True


class ControllerFilter(FileFilter):
    def name_filter(self, file_name):
        if 'Controller' in file_name and file_name.endswith('.java'):
            return False
        return True
