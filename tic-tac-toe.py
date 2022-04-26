"""
Assignment: 
    BYU-I, 2022 Spring Semester, Week 2
    CSE 210: W02 Prove: Developer - Solo Code Submission
Author: Seth Godoy
Purpose: Create a Tic-Tac-Toe game to play in a terminal
"""


def main():
    """The main function of the program that runs the game.

    Stores a list of strings of numbers to display in the board and starts
    a loop to play the game. The loop alternates between turns for X and O
    to place their symbols on the board. The loop ends when end_game equals True.
    """
    print('\n---- Tic-Tac-Toe ----')
    print('\nLet the game begin!')

    squares = create_squares()
    end_game = False
    while end_game == False:
        display_board(squares)
        choice = player_turn(squares, turn='X')
        squares[squares.index(choice)] = 'X'
        end_game = check_win(squares, turn='X')

        if end_game == False:
            display_board(squares)
            choice = player_turn(squares, turn='O')    
            squares[squares.index(choice)] = 'O'
            end_game = check_win(squares, turn='O')


def player_turn(squares, turn):
    """Fills the board with the appropriate mark of the player's turn.

    Asks player X or O to choose a square where to place their marks.
    The choice is first validated before returning the value.

    Args:
        squares (list): a list of strings of numbers, Xs or Os.
        turn (str): a string to tell who's turn it is.

    Return:
        choice (str): the square the player has chosen.
    """
    valid_choice = False
    while valid_choice == False:
        choice = input(f'It\'s {turn}\'s turn to choose a square(1-9).\n> ')

        if choice == 'X' or choice == '0':
            display_board(squares)
            print('You didn\'t enter a valid number.\n'
            'Please enter a valid number(1-9) that isn\'t already taken.\n')
            valid_choice = False 
        elif choice in squares:
            valid_choice = True
        else:
            display_board(squares)
            print('You didn\'t enter a valid number.\n'
            'Please enter a valid number(1-9) that isn\'t already taken.\n')
            valid_choice = False
    return choice


def check_win(squares, turn):
    """Checks if a player has won or if a draw has happened.

    Checks if a player has completed a row, a column, or a diagonal and
    checks if the board has been filled but nobody has won.

    Args:
        squares (list): a list of strings of numbers, Xs or Os.
        turn (str): a string to check who wins.

    Return:
        Boolean: False to continue game; True to end game. 
    """
    if \
    (squares[0] == turn and squares[1] == turn and squares[2] == turn) or \
    (squares[3] == turn and squares[4] == turn and squares[5] == turn) or \
    (squares[6] == turn and squares[7] == turn and squares[8] == turn) or \
    (squares[0] == turn and squares[3] == turn and squares[6] == turn) or \
    (squares[1] == turn and squares[4] == turn and squares[7] == turn) or \
    (squares[2] == turn and squares[5] == turn and squares[8] == turn) or \
    (squares[0] == turn and squares[4] == turn and squares[8] == turn) or \
    (squares[6] == turn and squares[4] == turn and squares[2] == turn):
        display_board(squares)
        print(f'{turn} wins!\nGood game. Thanks for playing!\n')
        return True

    else:
        filled_squares = 0
        for i in squares:
            if i == 'X' or i == 'O':
                filled_squares += 1
        
        if filled_squares == 9:
            display_board(squares)
            print('Draw!\nGood game. Thanks for playing!\n')
            return True
        else:
            return False


def display_board(squares):
    """Displays the board.

    Args:
        squares (list): a list of strings of numbers, Xs or Os.

    Returns: nothing.
    """
    print('\n'
    f'     {squares[0]} | {squares[1]} | {squares[2]}\n'
    '     ---------\n'
    f'     {squares[3]} | {squares[4]} | {squares[5]}\n'
    '     ---------\n'
    f'     {squares[6]} | {squares[7]} | {squares[8]}\n')


def create_squares():
    """Creates a list of numbers as strings to display in the board.

    Args: none.

    Returns:
        squares (list): a list of numbers as strings.
    """
    squares = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    return squares


if __name__ == '__main__':
    main()