"""
Assignment: W02 Prove: Developer - Solo Code Submission
Author: Seth Godoy
Purpose: Create a TUI(text-based user interface) to play Tic-Tac-Toe
"""


def main():
    sqrs = square_values()
    board = give_board(sqrs)
    play_game(sqrs, board)


def play_game(sqrs, board):
    end_game = False
    print(board)


def give_board(sqrs):
    board = '\n' \
    f'{sqrs[0]} | {sqrs[1]} | {sqrs[2]}\n' \
    '---------\n' \
    f'{sqrs[3]} | {sqrs[4]} | {sqrs[5]}\n' \
    '---------\n' \
    f'{sqrs[6]} | {sqrs[7]} | {sqrs[8]}\n'
    return board


def square_values():
    sqrs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return sqrs


if __name__ == '__main__':
    main()