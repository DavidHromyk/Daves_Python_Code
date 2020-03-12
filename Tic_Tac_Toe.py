def tboard_list():
    # Generate the list
    board_list = ['#']
    while len(board_list) < 10:
        r = input('Please select X or O: ')
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

def player_input():
    
    marker = ''
    # Ask player 1 to choose X 0
    while the marker != 'X' and marker != 'O':
        return input('Player 1, please select X or O')

    
    
print ('\n' * 5)
# Call the list for the board
tboard = tboard_list()

# Call the drawing of the board
draw_board(tboard)

def player_input():
    
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1 please select X or O: ')
        
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O','X')
