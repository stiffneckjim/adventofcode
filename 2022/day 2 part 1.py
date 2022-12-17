def score_game(opponent, player):
    # Win scores 6
    # Draw scores 3
    # Loss scores 0

    # Player is Rock
    if player == "X":
        # Opponent is Scissors - Win
        if opponent == "C":
            print("Rock beats Scissors: 6")
            return 6
        # Opponent is Rock - Draw
        if opponent == "A":
            print("Rock drows with Rock: 3")
            return 3

        # Opponent is Scissors - Lose
        print("Rock loses to Paper: 0")
        return 0

    # Player is Paper
    if player == "Y":
        # Opponent is Rock - Win
        if opponent == "A":
            print("Paper beats Rock: 6")
            return 6
        # Opponent is Paper - Draw
        if opponent == "B":
            print("Paper draws with Paper: 3")
            return 3
        # Opponent is Scissors - Lose
        print("Paper loses to Scissors: 0")
        return 0

    # Player is Scissors
    if player == "Z":
        # Opponent is Paper - Win
        if opponent == "B":
            print("Scissors beats Paper: 6")
            return 6
        # Opponent is Scissors - Draw
        if opponent == "C":
            print("Scissors draws with Scissors: 3")
            return 3

        print("Scissors loses to Rock: 0")
        # Opponent is Rock - Lose
        return 0


# with open("test.txt", "r") as f:
with open("day 2 input.txt", "r") as f:
    lines = f.readlines()

# A: Rock scores 1
# B: Paper scores 2
# C: Scissors score 3
play_names = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors",
}
plays = {"X": 1, "Y": 2, "Z": 3}

total = 0

for line in lines:
    # line = line.replace("\n", "")
    # print(f"Input: {line}")
    opponent, player = line.split()
    # print(f"Player: {play_names[player]}, Opponent: {play_names[opponent]}")
    score = plays[player] + score_game(opponent, player)
    total += score
    print(f"Score: {score}, Total: {total}")

print(f"Score: {total}")
