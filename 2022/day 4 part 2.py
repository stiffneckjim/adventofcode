def check_range(range1, range2):
    return (
        (range1[0] <= range2[0] and range1[1] >= range2[1])
        or (range2[0] <= range1[0] and range2[1] >= range1[1])
        or (range1[0] <= range2[0] and range1[1] >= range2[0])
        or (range1[0] <= range2[1] and range1[1] >= range2[1])
    )
    # print("Range 1 includes Range 2")
    # print(f"{range1[0]} <= {range2[0]} and {range1[1]} >= {range2[1]}"
    # print("Range 2 includes Range 1")
    # print(f"{range2[0]} <= {range1[0]} and {range2[1]} >= {range1[1]}")


count = 0

# with open("test.txt", "r") as f:
with open("day 4 input.txt", "r") as f:
    lines = f.readlines()


for line in lines:
    line = line.replace("\n", "")
    elf1, elf2 = line.split(",")

    print(f"Elf 1: {elf1} Elf 2: {elf2}")
    # Convert the ranges into integers
    if check_range(list(map(int, elf1.split("-"))), list(map(int, elf2.split("-")))):
        count += 1
        print(f"Overlap! Count: {count}")


print(f"Count: {count}")
