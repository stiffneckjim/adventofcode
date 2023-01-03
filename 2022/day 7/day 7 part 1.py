import re
import directory as dir

# dict for contents
# tuple for name and size


root = dir.Directory("root", "/")
breadcrumb = []

# with open("day 7 input.txt", "r") as f:
with open("test.txt", "r") as f:
    lines = f.readlines()

dir_ls = []
curr_dir = root
for i in range(len(lines)):

    line = lines[i].replace("\n", "")
    print(f"Next line: {line}")
    # Change directory
    if re.search(r"\$ cd", line):
        # Add new directory for breadcrumb
        dir_name = re.match(r"\$ cd (.+)", line).group(1)
        breadcrumb.append(dir_name)
        dir_path = "/".join(breadcrumb)
        print(f"New directory {dir_path}")
        curr_dir = curr_dir.child_dir(dir_name)

    # Read in result of 'ls' command
    elif re.match(r"\$ ls", line):
        curr_dir = True

    elif in_dir:
        # e.g. dir jpmf
        ls_re = re.match(r"(\w+) (\w+)", line)

        # New directory
        if ls_re.group(1) == "dir":
            filesystem = new_dir(ls_re.group(2), filesystem, breadcrumb)

        # New file
        else:
            print(f"File found: {ls_re.group(2)} with size {ls_re.group(1)}")
