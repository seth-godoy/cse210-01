"""
Assignment: W02 Prove: Developer - Solo Code Submission
Author: Seth Godoy
Purpose: Create a TUI(text-based user interface) to play Tic-Tac-Toe
"""


def main():
    squares = create_squares()
    play_game(squares)


def play_game(squares):
    end_game = False

    while end_game == False:
        valid_choice = False
        display_board(squares)
        
        while valid_choice == False:
            choice = input('It\'s X\'s turn to choose a square(1-9).\n> ')
            if choice == 'X' or choice == '0':
                print('\nYou didn\'t enter a valid number.\n'
                'Please enter a valid number(1-9) that isn\'t already taken.\n')
                valid_choice = False 
            elif choice in squares:
                valid_choice = True
            else:
                print('\nYou didn\'t enter a valid number.\n'
                'Please enter a valid number(1-9) that isn\'t already taken.\n')
                valid_choice = False

        squares[squares.index(choice)] = 'X'
        end_game = check_win(squares, turn='X')


def check_win(squares, turn):
    if turn == 'X':
        if \
        (squares[0] == 'X' and squares[1] == 'X' and squares[2] == 'X') or \
        (squares[3] == 'X' and squares[4] == 'X' and squares[5] == 'X') or \
        (squares[6] == 'X' and squares[7] == 'X' and squares[8] == 'X') or \
        (squares[0] == 'X' and squares[3] == 'X' and squares[6] == 'X') or \
        (squares[1] == 'X' and squares[4] == 'X' and squares[7] == 'X') or \
        (squares[2] == 'X' and squares[5] == 'X' and squares[8] == 'X') or \
        (squares[0] == 'X' and squares[4] == 'X' and squares[8] == 'X') or \
        (squares[6] == 'X' and squares[4] == 'X' and squares[2] == 'X'):
            display_board(squares)
            print('X wins!\nThanks for playing!\n')
            return True
        else:
            return False


def display_board(squares):
    print('\n'
    f'{squares[0]} | {squares[1]} | {squares[2]}\n'
    '---------\n'
    f'{squares[3]} | {squares[4]} | {squares[5]}\n'
    '---------\n'
    f'{squares[6]} | {squares[7]} | {squares[8]}\n')


def create_squares():
    squares = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    return squares


if __name__ == '__main__':
    main()