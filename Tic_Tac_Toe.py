
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
        t = input(f'Player 2 place {player_2}: ')
        if r == 'X' or r =='O':
            board_list.append(r)
        elif t == 'X' or t == 'O':
            board_list.append(t)
            
                
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
    marker = 'X'
    if board[7] == marker and board[8] == marker and board[9] == marker:
        return ('Player 1 wins!')
    if board[4] == marker and board[5] == marker and board[6] == marker:
        return ('Player 1 wins!')
    if board[1] == marker and board[2] == marker and board[3] == marker:
        return ('Player 1 wins!')
    if board[7] == marker and board[4] == marker and board[1] == marker:
        return ('Player 1 wins!')
    if board[8] == marker and board[5] == marker and board[2] == marker:
        return ('Player 1 wins!')
    if board[9] == marker and board[6] == marker and board[3] == marker:
        return ('Player 1 wins!')

