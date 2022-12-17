with open("input.txt", "r") as f:
    lines = f.readlines()

total = 0
high_scores = [0, 0, 0]

for line in lines:
    line = line.replace("\n", "")
    # This only works because there's an empty line at the end of the file
    if line == "":
        if total > high_scores[0]:
            high_scores[0] = total
            high_scores = sorted(high_scores)
            print(f"High scores: {high_scores[0]}, {high_scores[1]}, {high_scores[2]}")

        total = 0
    else:

        total += int(line)
        # print(f"Total: {total}")

print(f"High scores total: {sum(high_scores)}")
