import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_turn = input("Your choices are: Rock, Paper or Scissors! Chose wisely!\n")

if player_turn == "Rock":
    player_turn = rock
elif player_turn == "Paper":
    player_turn = paper
elif player_turn == "Scissors":
    player_turn = scissors
else:
    raise SystemExit("Invalid Input. Try again...")

computer_random_number = random.randint(1, 3)
computer_move = ""

if computer_random_number == 1:
    computer_move = "Rock"
elif computer_random_number == 2:
    computer_move = "Paper"
elif computer_random_number == 3:
    computer_move = "Scissors"

print(f"The computer chose {computer_move}")

if player_turn == rock and computer_move == scissors or \
        player_turn == paper and computer_move == rock or \
        player_turn == scissors and computer_move == paper:
    print("You win!")
elif player_turn == computer_move:
    print("Draw!")
else:
    print("You lose!")
