import random
from IPython.display import clear_output

hands = [1,2,3]
players = ['Player 1','Computer']

while True:
    
    
    play = input('Would you like to play Rock, Paper, Scissors?: ')

    
    if play.lower()[0] == 'y':
        
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
         
        computer_choice = random.choice(hands)
        
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
        
        # Check winning conditions
        
        if choice == 1 and computer_choice == 1 or choice == 2 and computer_choice == 2 or choice == 3 and computer_choice ==3:
            print ('\nDraw!')
        if choice == 1 and computer_choice == 2 or choice == 3 and computer_choice == 1 or choice == 2 and computer_choice ==3:
            print ('\nComputer Wins!')
        if choice == 1 and computer_choice == 3 or choice == 2 and computer_choice == 1 or choice == 3 and computer_choice ==2:
            print ('\nYou Win!')
            
        again = input("Would you like to play again?: ")
        
        if again.lower()[0] == 'y':
            continue
        else:
            clear_output()
            print("We'll see you next time!")
            break 
            
    else:
        clear_output()
        print("Maybe next time")
        break
