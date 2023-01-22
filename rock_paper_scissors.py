import random
from stringcolor import *

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
play = True

while play:
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
        print(cs("You win!", "Lime"))
    elif player_turn == computer_move:
        print(cs("Draw!", "Grey"))
    else:
        print(cs("You lose!", "Red"))

    play_or_quit = input("Do you want to continue playing?\nType \"Yes\" to continue or \"No\" to exit.\n")
    if play_or_quit == "Yes":
        continue
    elif play_or_quit == "No":
        print("Exiting...")
        play = False
