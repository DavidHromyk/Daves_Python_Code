def player_input():
    
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1 please select X or O: ')
        
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O','X')
    
player_1,player_2 = player_input()

print ('\n' * 2)
print (f'Player 1 is {player_1}')
print (f'Player 2 is {player_2}')



print ('\n' * 3)
def tboard_list():
    # Generate the list
    board_list = ['#']
    while len(board_list) < 10:
        r = input(f'Player 1 place {player_1}: ')

        if r == 'X' or r =='O':
            board_list.append(r)

            
                
    return board_list

tboard = tboard_list()


def draw_board(board):
    
    
# Print the board
    print (board[7] + '|' + board[8] + '|' + board[9] + '|')
    print ('------')
    print (board[4] + '|' + board[5] + '|' + board[6] + '|')
    print ('------')
    print (board[1] + '|' + board[2] + '|' + board[3] + '|')


    
    # Return the win if there are 3 in a row
    
def place_marker(board, marker, position):
    board[position] = marker


def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

print ('\n' * 2)
position = player_choice(draw_board)
place_marker(tboard,player_1,position)
draw_board(tboard)
