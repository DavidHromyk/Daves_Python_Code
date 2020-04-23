import random
from IPython.display import clear_output
def check_win(choice,computer_choice):
    if choice == 1 and computer_choice == 1 or choice == 2 and computer_choice == 2 or choice == 3 and computer_choice ==3:
        print ('\nDraw!')
    if choice == 1 and computer_choice == 2 or choice == 3 and computer_choice == 1 or choice == 2 and computer_choice ==3:
        print ('\nComputer Wins!')
    if choice == 1 and computer_choice == 3 or choice == 2 and computer_choice == 1 or choice == 3 and computer_choice ==2:
        print ('\nYou Win!')

def play_again():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
    
def playing():
    hands = [1,2,3]
    players = ['Player 1','Computer']
    computer_choice = random.choice(hands)

    clear_output()
    print("------------------------------")
    print("Welcome to Rock Paper Scissors")
    print("------------------------------")

    print("\nPlease Select\n1. Rock \n2. Paper\n3. Scissors")

    try:
        choice = int(input("Please select rock, paper, or scissors: "))


    except:
        clear_output()
        choice = int(input("Try again. Please select rock, paper, or scissors: "))

            

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
    print(f"Your choice is {choice_name}")
    print(f"\nComputer choice is {computer_choice_name}")
    
    check_win(choice,computer_choice)
            

    def main():
        
    while True:
        play = input('Would you like to play Rock, Paper, Scissors?: ')
        
        if play.lower()[0] == 'y':
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
            break
main()
