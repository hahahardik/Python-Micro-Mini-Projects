# TIC-TAC-TOE

import random

# Displaying the board, the entries are stored in a list with the indexes as on the numpad.
def display_board(board):
    
    print(f'{board[7]} | {board[8]} | {board[9]}')
    print(f'{board[4]} | {board[5]} | {board[6]}')
    print(f'{board[1]} | {board[2]} | {board[3]}')


# Getting the player input and storing them in global variables p1 and p2 so that we dont't need to assign them again.
def player_input():
    
    global p1, p2
    
    choices = ['X', 'O']
    p1 = 'Z'
    
    while p1 not in choices:

        p1 = input('Player 1: Choose "X" or "O": ')
        if p1 == 'X':
            p2 = 'O'
            print(f'Player 2: You get {p2}\n')
        elif p1 == 'O':
            p2 = 'X'
            print(f'Player 2: You get {p2}\n')
        else:
            print('Please choose among "X" and "O" only.\n')


# Assigning the marker ('X' or 'O') on the desired position (1-9), entered via numpad.
def place_marker(board, marker, position):
    board[position] = marker


# Check if the present board wins the streak of three for given the specified marker ('X' or 'O')
def win_check(board, mark):
    
    if board[7] == board[8] == board[9] == mark or
    board[4] == board[5] == board[6] == mark or
    board[1] == board[2] == board[3] == mark or
    board[7] == board[4] == board[1] == mark or
    board[8] == board[5] == board[2] == mark or     
    board[9] == board[6] == board[3] == mark or
    board[7] == board[5] == board[3] == mark or
    board[9] == board[5] == board[1] == mark
    else:
        return False


# Choose a random player to go first
def choose_first():
    
    players = ['p1', 'p2']
    choice = random.choice(players)
    
    if choice == 'p1':
        return 'Player 1'
    else:
        return 'Player 2'


# Check if the there is space on the board for a position
def space_check(board, position):
    
    if board[position] == ' ':
        return True
    else:
        return False


# Check if the complete board has any space or not
def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


# Ask the player for his choice and check if that position is empty on the board and in range 1-9
def player_choice(p, board):
    
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input(f'{p} Choose your position: (1-9) '))
        
    return position


# Check if the player wants to replay or not
def replay():
    
    #returns true if the input starts with 'y'
    return input('\nDo you want to play again? Enter Yes or No: ').lower().startswith('y')



# ----------------------------------------------------------------------------------------------------------------
# Final Assembly

print('Welcome to Tic Tac Toe!\n')

#Initial condition
while True:
    
    # Reset the board
    theBoard = [' '] * 10
    #Ask for the player input
    player_input()
    # Randomly choose first and save the player's name in variable 'turn'
    turn = choose_first()
    print(turn + ' you will go first!\n')
    
    
    #Ask if the are ready?
    play_game = input('Are you ready to play? Enter Yes or No.')
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
        
        
    while game_on:
        
        if turn == 'Player 1':
            # Player1's turn.
            
            #Display the reset board
            display_board(theBoard)
            #Ask for choice and if it is available, store it in postion or ask again
            position = player_choice(turn, theBoard)
            #Mark that position on the board
            place_marker(theBoard, p1, position)
            
            #Check if there's a winning combination
            if win_check(theBoard, p1):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            #Else check if the board is full (In that case the game is a draw) else, pass the turn to player 2
            else:
                
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
            
        else:
            # Player2's turn.
            
            #Similar as for Player 1
            
            display_board(theBoard)
            position = player_choice(turn, theBoard)
            place_marker(theBoard, p2, position)

            if win_check(theBoard, p2):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'
                    
    #Display the replay msg after result
    #If no...exit
                    
    if not replay():
        print('\nThank You!\n')
        break

#End
#-------------------------------------------------------------------------------------------------------------