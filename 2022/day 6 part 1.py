def find_dupes(str):

    if len(str) == 1:
        print(f"Not found")
        return False
    print(f"Search {str[1:]} for {str[0]}")

    if str.find(str[0], 1) >= 0:
        return True
    else:
        return find_dupes(str[1:])


# with open("test.txt", "r") as f:
with open("day 6 input.txt", "r") as f:
    lines = f.readlines()

for line in lines:

    line = line.replace("\n", "")
    for i in range(len(line) - 3):
        if find_dupes(line[i : i + 4]) == False:
            print(f"Result: {i + 4}")
            exit()

print("No marker found!")
