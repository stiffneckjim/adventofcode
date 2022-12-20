import re


stack_lines = []

# Read stack
def read_stacks(stack_lines, labels):

    stacks = {}
    for label in labels:
        # Populate stacks with empty strings
        stacks[label] = []
    # Preprocessing :)
    # Replace every 4th space with a comma
    for line in stack_lines:
        line = line.replace("[", "")
        line = line.replace("] ", ",").replace("]", "")
        line = line.replace("    ", " ,")
        line = line.split(",")

        # print(line)

        for i in range(len(labels)):
            if line[i] != " ":
                stacks[labels[i]].append(line[i])
                # print(f"{labels[i]}: {line[i]}")

    return stacks


def max_height(stacks):
    max = 0
    for label in stacks.keys():
        if max < len(stacks[label]):
            max = len(stacks[label])

    print(f"Height: {max}")
    return max


def pretty_print(stacks):
    height = max_height(stacks)
    for row in range(height - 1, -1, -1):
        line = ""
        for label in stacks.keys():
            if row < len(stacks[label]):
                line = line + "[" + stacks[label][row] + "]"
            else:
                line = line + "   "

        print(line)

    hr = ""
    labels = ""
    for label in stacks.keys():
        hr = hr + "---"
        labels = labels + " " + label + " "

    print(hr)
    print(labels)


def move_crates(stacks, count, source, dest):
    print(f"Count: {count} Source: {source} Destination: {dest}")
    for _ in range(count):
        stacks[dest].append(stacks[source].pop())

    return stacks


# with open("test.txt", "r") as f:
with open("day 5 input.txt", "r") as f:
    lines = f.readlines()

for line in lines:

    line = line.replace("\n", "")
    # Read in the stacks and add them to a list
    if line.find("[") >= 0:
        stack_lines.insert(0, line)

    # Stack labels row regexp
    elif re.match(r" (\d+ +){1,}", line):
        labels = line.split()
        print(f"Stack label {labels}")
        # Build stacks
        stacks = read_stacks(stack_lines, labels)

        # pretty_print(stacks)

    else:
        instr = re.match(
            r"move (?P<count>\d+) from (?P<source>\d+) to (?P<dest>\d+)", line
        )
        if instr:
            move_crates(
                stacks,
                int(instr.group("count")),
                instr.group("source"),
                instr.group("dest"),
            )
            # pretty_print(stacks)

pretty_print(stacks)
result = "Result:"
for label in labels:
    if len(stacks[label]) > 0:
        result = result + stacks[label][-1]
    else:
        result = result + " "
print(result)
