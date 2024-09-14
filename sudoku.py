from input import input
from colorama import Fore, Style, init

init(autoreset=True)

board = input()

def print_borders(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)  # Horizontal border

        row_to_print = ""
        for j in range(9):
            if j % 3 == 0 and j != 0:
                row_to_print += Fore.WHITE + "| "

            # Check the value and assign color
            number = board[i][j]
            if number == 0:
                row_to_print += Fore.BLACK + "0 "  # Red for empty spaces
            else:
                row_to_print += Fore.WHITE + str(number) + " "

        print(row_to_print)

print_borders(board)