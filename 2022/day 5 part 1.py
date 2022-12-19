import re


stacks = {}
stack_lines = []

# Read stack
def read_stacks(stacks, stack_line):

    # Preprocessing :)
    # Replace every 4th space with a comma
    for x in range(len(line) // 4):
        stack = line[(x * 4) + 1]
        print(f"{x}: {stack}")
        if stack != " ":
            # Check if a stack exists
            stacks[x].append(stack)

    print(f"{stacks}")


# with open("day 5 input.txt", "r") as f:
with open("test.txt", "r") as f:
    lines = f.readlines()

for line in lines:

    line = line.replace("\n", "")
    # Read in the stacks and add them to a list
    if line.find("[") >= 0:
        print(f"{len(line)}")
        stack_lines.append(line)

    # Stack labels row regexp
    if re.match(r" (\d+ +){1,}", line):
        print(f"Stack label {line.split()}")
