import random
import os
import sys

player_wins = 0
computer_wins = 0


def check_win(choice, computer_choice):
    global computer_wins
    global player_wins
    if choice == 1 and computer_choice == 1 or choice == 2 and computer_choice == 2 or choice == 3 and computer_choice == 3:
        print('\nDraw!')
        print("_____________________________")
    if choice == 1 and computer_choice == 2 or choice == 3 and computer_choice == 1 or choice == 2 and computer_choice == 3:
        print('\nComputer Wins!')
        print("_____________________________")
        computer_wins = computer_wins + 1
        print(f"\nComputer wins {computer_wins}")
        print(f"\nPlayer 1 wins {player_wins}")
    if choice == 1 and computer_choice == 3 or choice == 2 and computer_choice == 1 or choice == 3 and computer_choice == 2:
        print('\nYou Win!')
        print("_____________________________")
        player_wins = player_wins + 1
        print(f"\nPlayer 1 wins {player_wins}")
        print(f"\nComputer wins {computer_wins}")

    if computer_wins == 3:
        sys.exit("Computer has won it all!\n")
    if player_wins == 3:
        sys.exit("Player 1 has won it all!\n")


def playing():
    hands = [1, 2, 3]
    computer_choice = random.choice(hands)

    print("\nPlease Select\n1. Rock \n2. Paper\n3. Scissors")

    try:
        choice = int(input("\nPlease select rock, paper, or scissors: "))

    except:
        os.system('cls')
        choice = int(
            input("Try again. Please Select\n\n1. Rock \n2. Paper\n3. Scissors: "))

    if choice > 3:
        choice = random.choice(hands)
    if choice == 1:
        choice_name = "rock"
    elif choice == 2:
        choice_name = "paper"
    else:
        choice_name = "scissors"

    if computer_choice == 1:
        computer_choice_name = "rock"
    elif computer_choice == 2:
        computer_choice_name = "paper"
    else:
        computer_choice_name = "scissors"

    os.system('cls')
    print("_____________________________")
    print(f"\nYour choice is {choice_name}")
    print(f"\nComputer choice is {computer_choice_name}")

    check_win(choice, computer_choice)


def main():

    while True:
        play = input('\nWould you like to play Rock, Paper, Scissors?: ')

        if play.lower()[0] == 'y':
            os.system('cls')
            print("------------------------------")
            print("Welcome to Rock Paper Scissors")
            print("------------------------------")

            gaming = True
        else:
            gaming = False

        if gaming == True:
            playing()

        else:
            os.system('cls')
            print("Maybe we'll play next time")
            break


main()
