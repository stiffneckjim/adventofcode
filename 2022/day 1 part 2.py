with open("input.txt", "r") as f:
    lines = f.readlines()

high_score = 0
totals = [0, 0, 0]

for line in lines:
    line = line.replace("\n", "")
    # print(line)
    if line == "":
        if total > high_score:
            high_score = total

        total = 0
    else:

        total += int(line)
        # print(f"Total: {total}")

print(f"High score total: {high_score}")

