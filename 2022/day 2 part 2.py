def score_game(opponent, outcome):
    # Win scores 6
    # Draw scores 3
    # Loss scores 0
    outcomes = {"Win": 6, "Draw": 3, "Lose": 0}

    # Rock scores 1
    # Paper scores 2
    # Scissors scores 3
    shapes = {"Rock": 1, "Paper": 2, "Scissors": 3}

    if outcome == "Win":
        if opponent == "Rock":
            print("Win - Paper beat Rock")
            return outcomes["Win"] + shapes["Paper"]
        if opponent == "Paper":
            print("Win - Scissors beat Paper")
            return outcomes["Win"] + shapes["Scissors"]
        if opponent == "Scissors":
            print("Win - Rock beats Scissors")
            return outcomes["Win"] + shapes["Rock"]

    if outcome == "Draw":
        if opponent == "Rock":
            print("Draw - Rock draws with Rock")
            return outcomes["Draw"] + shapes["Rock"]
        if opponent == "Paper":
            print("Draw - Paper draws with Paper")
            return outcomes["Draw"] + shapes["Paper"]
        if opponent == "Scissors":
            print("Draw - Scissors draws with Scissors")
            return outcomes["Draw"] + shapes["Scissors"]

    if outcome == "Lose":
        if opponent == "Rock":
            print("Lose - Scissors loses to Rock")
            return outcomes["Lose"] + shapes["Scissors"]
        if opponent == "Paper":
            print("Lose - Rock loses to Paper")
            return outcomes["Lose"] + shapes["Rock"]
        if opponent == "Scissors":
            print("Lose - Rock loses to Scissors")
            return outcomes["Lose"] + shapes["Paper"]


with open("day 2 input.txt", "r") as f:
    # with open("test.txt", "r") as f:
    lines = f.readlines()

# Rock scores 1
# Paper scores 2
# Scissors score 3
code_names = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Lose",
    "Y": "Draw",
    "Z": "Win",
}

total = 0

for line in lines:
    # line = line.replace("\n", "")
    # print(f"Input: {line}")
    opponent, outcome = line.split()
    print(f"Opponent: {code_names[opponent]}, Outcome: {code_names[outcome]}")
    score = score_game(code_names[opponent], code_names[outcome])
    total += score
    print(f"Score: {score} Total: {total}")
