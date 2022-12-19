from itertools import islice


def lookup_priority(char):
    return "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".index(char) + 1


# Take a string and split it into two lists
def split_line(line):
    length = len(line) // 2
    print(f"Length: {length}")
    return list(line)[:length], list(line)[length:]


def find_duplicates(first, second):
    dupes = []
    for i in range(len(first)):
        for j in range(len(second)):
            if first[i] == second[j]:
                dupes.append(first[i])

    return dupes


def find_duplicate(left, right):
    for i in range(len(left)):
        for j in range(len(right)):
            if left[i] == right[j]:
                return left[i]


total = 0

# with open("test.txt", "r") as f:
with open("day 3 input.txt", "r") as f:
    while True:

        lines = list(islice(f, 3))

        if not lines:
            break

        print(f"Input: {lines[0]}")
        print(f"Input: {lines[1]}")
        print(f"Input: {lines[2]}")

        dupes = find_duplicates(lines[0], lines[1])
        char = find_duplicate(dupes, lines[2])
        print(f"Pass: {char}")
        score = lookup_priority(char)
        total += score
        print(f"Score: {score}, Total: {total}")

print(f"Total: {total}")
