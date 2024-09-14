from input import input
from colorama import Fore, Style, init

init(autoreset=True)

board = input()

cols = input()
for x in cols:
    for y in range(len(x)):
        x[y]=511 if x[y]==0 else 0
#print(cols)

rows = [[col[i] for col in cols] for i in range(len(board))]
#print(rows)

boxes = [[] for _ in range(9)]
for row in range(9):
    for col in range(9):
        box_index = (row // 3) * 3 + (col // 3)
        boxes[box_index].append(board[row][col])
#print(boxes)

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
            if number == 0 :
                row_to_print += Fore.BLACK + "0 "  # Red for empty spaces
            else:
                row_to_print += Fore.WHITE + str(number) + " "

        print(row_to_print)
    print()

print_borders(board)