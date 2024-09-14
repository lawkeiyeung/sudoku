from input import input

board = input()

def print_sudoku_with_borders(board):
    for i in range(9):
        # Print horizontal border after every 3 rows
        if i % 3 == 0 and i != 0:
            print("-" * 21)  # 21 dashes to cover grid width (including borders)

        row_to_print = ""
        for j in range(9):
            # Print vertical border after every 3 columns
            if j % 3 == 0 and j != 0:
                row_to_print += "| "

            # Print each number, using 0 as a placeholder for empty spaces
            row_to_print += str(board[i][j]) + " "

        # Print the constructed row
        print(row_to_print)

print_sudoku_with_borders(board)