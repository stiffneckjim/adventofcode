import file as f


class Directory(f.File):

    file_list = {}
    dir_list = {}

    def is_root(self):
        if self.parent is None:
            return True

        return False

    def add_file(self, name, size):
        self.file_list[name] = f.File(name, size)
        self.size += size

        return self

    def add_dir(self, name, path):
        self.dir_list[name] = Directory(name, path)
        return self

    def child_dir(self, name):
        return self.dir_list[name]

    def pretty_print(self, indent=""):
        print(f"{indent} {self.name}")
        for f in self.file_list:
            f.pretty_print(indent + " ")

        for dir in self.dir_list:
            dir.pretty_print(indent + "-")
