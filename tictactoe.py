# Declare Global Variables

board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
game_still_going = True
current_player = 'X'
winner = None


def check_rows():
    global game_still_going
    # check row one
    row1 = board[0] == board[1] == board[2] != '-'
    # check row two
    row2 = board[3] == board[4] == board[5] != '-'
    # check row three
    row3 = board[6] == board[7] == board[8] != '-'
    if row1 or row2 or row3:
        game_still_going = False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return


def check_columns():
    global game_still_going
    # check row one
    col1 = board[0] == board[3] == board[6] != '-'
    # check row two
    col2 = board[1] == board[4] == board[7] != '-'
    # check row three
    col3 = board[2] == board[5] == board[8] != '-'
    if col1 or col2 or col3:
        game_still_going = False
    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]
    return


def check_diagonals():
    global game_still_going
    # check row one
    diag1 = board[0] == board[4] == board[8] != '-'
    # check row two
    diag2 = board[2] == board[4] == board[6] != '-'

    if diag1 or diag2:
        game_still_going = False
    if diag1:
        return board[0]
    elif diag2:
        return board[2]

    return


def check_for_winner():
    global winner
    # Check Rows
    row_winner = check_rows()
    # Check Columns
    column_winner = check_columns()
    # Check Diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


def check_for_tie():
    global game_still_going
    if '-' not in board:
        game_still_going = False

    pass


def check_if_game_over():
    check_for_winner()
    check_for_tie()


def flip_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'
    pass


def play_game():
    # Display initial board
    display_board()

    while game_still_going:
        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    if winner == 'X' or winner == 'O':
        print(f'{winner} won')
    else:
        print(f'Game is a Tie')


def display_board():
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print(f'{board[6]} | {board[7]} | {board[8]}')


def handle_turn(player):
    player_input = ''
    position = 0

    while player_input != '-':
        print(f'{player}\'s turn.')

        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            position = input('Choose a position from 1-9: ')

        position = int(position) - 1
        player_input = board[position]
    board[position] = f'{player}'

    display_board()


play_game()
