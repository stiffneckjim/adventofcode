size_len = 5


class File:

    name = ""
    size = 0
    parent = None

    # Add a new directory into the filesystem at the breadcrumb location
    def __init__(self, name, parent, size=0):
        self.name = name
        self.parent = parent
        self.size = size
        if len(str(size)) > size_len:
            size_len = len(str(size))

    def pretty_print(self, indent="-"):
        size_str = str(self.size).rjust(size_len, " ")
        print(f"{indent} {self.name}: {size_str}")
