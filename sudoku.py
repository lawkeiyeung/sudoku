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
                elif number <0:
                    row_to_print += Fore.RED + str(number*-1) + " "  # Red for empty spaces
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
def calpossible():
    min_value = float('inf')
    min_indexes = None
    for x in range(9):
        for y in range(9):
            if possible[x][y][0] >0:
                for num in board[x]:
                    if num < 0:
                        num=num*-1
                    if num != 0:
                        possible[x][y][0]=clear_bit_at_position(possible[x][y][0],(num-1))
                for num in rows[y]:
                    if num < 0:
                        num=num*-1
                    if num != 0:
                        possible[x][y][0]=clear_bit_at_position(possible[x][y][0],(num-1))
                for num in boxes[(((x)//3)*3)+(y)//3]:
                    if num < 0:
                        num=num*-1
                    if num != 0:
                        possible[x][y][0]=clear_bit_at_position(possible[x][y][0],(num-1))
                possible[x][y][1]=(bin(possible[x][y][0]).count('1'))-1
                if possible[x][y][1] < min_value:
                    min_value = possible[x][y][1]
                    min_indexes = (y, x)
    return min_value,min_indexes

def fill(number,x,y):
    board[x][y]=number
    rows[y][x]=number
    boxes[x//3*3+y//3][y%3*3+x%3]=number
    possible[x][y]=[-1,10]

def fillbox(min_value,min_indexes):
    if min_value==1:
        #board[min_indexes[1]][min_indexes[0]]
        first_one_index = bin(possible[min_indexes[1]][min_indexes[0]][0])[2:].find('1', 1)
        number=-1*(10-first_one_index)
        x=min_indexes[1]
        y=min_indexes[0]
        fill(number,x,y)

    elif min_value>1:

        for a in range(9):
            blist=[]
            search=possible[a]
            for x in search:
                if x[0] != -1:
                    blist.append(x[0])
            if len(blist)>0:
                max_bits = max(number.bit_length() for number in blist)
                bit_counts = [0] * max_bits
                only_fill = [-1] * max_bits
                pos=0
                for number in blist:
                    for bit_position in range(max_bits):
                        if (number >> bit_position) & 1:
                            bit_counts[bit_position*-1-1] += 1
                            only_fill[bit_position*-1-1]=pos
                    pos+=1
                for x in range(1,10):
                    if bit_counts[x]==1:
                        for i in range(len(search)):
                            if search[i][0] == blist[only_fill[x]]:
                                fill((10-x)*-1,a,i)



def solve(x=1,printall=False):
    for i in range(x):
        min_value,min_indexes=calpossible()
        fillbox(min_value,min_indexes)
        if printall:
            print_borders(board)
    if not printall:
        print_borders(board)





print_borders(board)
min_value,min_indexes=calpossible()
fillbox(2,(min_indexes))
print_borders(board)

solve(45)


'''
print("~~~~~~~~")
print(board)
print("~~~~~~~~")
print(rows)
print("~~~~~~~~")
print(boxes)
print(possible)
print_borders(possible,2)


print(f"The minimum value is at index: {min_indexes[0]+1},{min_indexes[1]+1}")
print(f"The corresponding sublist is: {possible[min_indexes[1]][min_indexes[0]]}")
print_borders(possible,2)
print(min_indexes[0],min_indexes[1])
print((((min_indexes[1])//3)*3)+(min_indexes[0])//3,(((min_indexes[0])//3)*3)+(min_indexes[1])//3)
print(boxes[(((min_indexes[1])//3)*3)+(min_indexes[0])//3])
'''