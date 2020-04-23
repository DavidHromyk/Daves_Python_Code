import random
from IPython.display import clear_output
import sys

player_wins = 0
computer_wins = 0


def check_win(choice,computer_choice):
    
    if choice == 1 and computer_choice == 1 or choice == 2 and computer_choice == 2 or choice == 3 and computer_choice ==3:
        print ('\nDraw!')
        print("_____________________________")
    if choice == 1 and computer_choice == 2 or choice == 3 and computer_choice == 1 or choice == 2 and computer_choice ==3:
        print ('\nComputer Wins!')
        print("_____________________________")
        global computer_wins
        computer_wins = computer_wins + 1
        print(f"\nComputer wins {computer_wins}")
    if choice == 1 and computer_choice == 3 or choice == 2 and computer_choice == 1 or choice == 3 and computer_choice ==2:
        print ('\nYou Win!')
        print("_____________________________")
        global player_wins
        player_wins = player_wins + 1
        print(f"\nPlayer 1 wins {player_wins}")
    
    if computer_wins == 3:
        sys.exit("Computer has won it all!")
    if player_wins == 3:
        sys.exit("Player 1 has won it all!")

def play_again():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
    
def playing():
    hands = [1,2,3]
    computer_choice = random.choice(hands)

    print("\nPlease Select\n1. Rock \n2. Paper\n3. Scissors")

    try:
        choice = int(input("Please select rock, paper, or scissors: "))


    except:
        clear_output()
        choice = int(input("Try again. Please Select\n\n1. Rock \n2. Paper\n3. Scissors: "))

            

    if choice == 1:
        choice_name = "rock"
    elif choice == 2 :
        choice_name = "paper"
    else:
        choice_name = "scissors"


    if computer_choice == 1:
        computer_choice_name = "rock"
    elif computer_choice == 2:
        computer_choice_name = "paper"
    else:
        computer_choice_name = "scissors"

    clear_output()
    print("_____________________________")
    print(f"\nYour choice is {choice_name}")
    print(f"\nComputer choice is {computer_choice_name}")
    
    check_win(choice,computer_choice)
            

def main():       
    
    while True:
        play = input('Would you like to play Rock, Paper, Scissors?: ')
        
        if play.lower()[0] == 'y':
            clear_output()
            print("------------------------------")
            print("Welcome to Rock Paper Scissors")
            print("------------------------------")
            
            gaming = True
        else:
            gaming = False


        if gaming == True:
            playing()
            
        else:
            clear_output()
            print("Maybe we'll play next time")
            break
        
        if not play_again():
            clear_output()
            print('Maybe another time')
            break
main()
