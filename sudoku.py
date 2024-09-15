from input import input
from colorama import Fore, Style, init

init(autoreset=True)

board = input()

possible = input()
for x in possible:
    for y in range(len(x)):
        x[y]=[1023,9] if x[y]==0 else [-1,10]
#print(possible)

rows = [[col[i] for col in board] for i in range(len(board))]
#print(rows)

boxes = [[] for _ in range(9)]
for row in range(9):
    for col in range(9):
        box_index = (row // 3) * 3 + (col // 3)
        boxes[box_index].append(board[row][col])
#print(boxes)

def print_borders(board,base=10):
    if base == 10:
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
    else:
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("-" * 21)  # Horizontal border

            row_to_print = ""
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    row_to_print += Fore.WHITE + "| "

                # Check the value and assign color
                number = board[i][j][0] if board[i][j][0]==-1 else board[i][j][1]
                if number == -1 :
                    row_to_print += Fore.BLACK + "0 "  # Red for empty spaces
                else:
                    row_to_print += Fore.WHITE + str(number) + " "

            print(row_to_print)
    print()


def clear_bit_at_position(binary_num, pos):
    if isinstance(binary_num, str):
        binary_num = int(binary_num, 2)

    mask = ~(1 << pos)

    return binary_num & mask

# cal possible
for x in range(9):
    for y in range(9):
        if possible[x][y][0] >0:
            for col in board[x]:
                if col != 0:
                    possible[x][y][0]=clear_bit_at_position(possible[x][y][0],(col-1))
            for row in rows[y]:
                if row != 0:
                    possible[x][y][0]=clear_bit_at_position(possible[x][y][0],(row-1))
            for box in boxes[(((x)//3)*3)+(y)//3]:
                if box != 0:
                    possible[x][y][0]=clear_bit_at_position(possible[x][y][0],(box-1))
            possible[x][y][1]=(bin(possible[x][y][0]).count('1'))-1

print_borders(board)
print_borders(possible,2)