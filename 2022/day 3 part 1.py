def lookup_priority(char):
    return "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".index(char) + 1


# Take a string and split it into two lists
def split_line(line):
    length = len(line) // 2
    print(f"Length: {length}")
    return list(line)[:length], list(line)[length:]


def find_duplicate(left, right):
    for i in range(len(left)):
        for j in range(len(right)):
            if left[i] == right[j]:
                return left[i]


# with open("test.txt", "r") as f:
with open("day 3 input.txt", "r") as f:
    lines = f.readlines()


total = 0

for line in lines:
    line = line.replace("\n", "")
    print(f"Input: {line}")
    left, right = split_line(line)
    print(f"Left: {left}, Right: {right}")

    char = find_duplicate(left, right)
    print(f"Duplicate: {char}")
    score = lookup_priority(char)
    total += score
    print(f"Score: {score}, Total: {total}")

print(f"Total: {total}")
