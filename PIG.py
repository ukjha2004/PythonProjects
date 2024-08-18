import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)

    return roll

while True:
    players = int(input("Enter the number of players[2 - 4]: "))
    if 2 <= players <= 4:
        break
    else:
        print("Enter between 2-4 players.")



max_score = 50
players_scores= [0 for _ in range(players)]
while max(players_scores)< max_score:
    for players_idx in range(players):
        print("\nPlayer number", players_idx +1, "turn has just started!\n")
        print("Your total score is:", players_scores[players_idx],"\n")
        current_score = 0
        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a: ", value)
            print("Your score is:", current_score)

        players_scores[players_idx] += current_score
        print("Your total score is:", players_scores[players_idx])

max_score = max(players_scores)
winning_idx = players_scores.index(max_score)
print("Player number", winning_idx + 1, "is the winner with a score of:", max_score)