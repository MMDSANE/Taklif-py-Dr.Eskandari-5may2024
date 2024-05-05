import random  

MOUSE = "\U0001F401"
CHEESE = "\U0001F9C0"

n = 10
MATRIX = []
num = n ** 2

mouse_row = 4
mouse_col = 5

cheese_row = 8
cheese_col = 8

for i in range(n): 
    row = []
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or j == n-1:
            row.append(0)
        else:
            if i == mouse_row and j == mouse_col:
                row.append(MOUSE)
            elif i == cheese_row and j == cheese_col:
                row.append(CHEESE)
            else:
                row.append(random.randint(0, 1))
    MATRIX.append(row)


for i in range(n):
    for j in range(n):
        print(f"{MATRIX[i][j]}" , end="\t")
    print()
print("\n , \n")

flag = 0
while (mouse_row, mouse_col) != (cheese_row, cheese_col):
    # mouse_row, mouse_col = 3 , 3
    # cheese_row, cheese_col = 3 , 3
    if mouse_row < cheese_row:
        mouse_row += 1
        if mouse_row == 1:
            flag = 0
        else:
            flag = 1
        if flag == 1:
            mouse_row -= 1
        else:
            pass

    elif mouse_row > cheese_row:
        mouse_row -= 1
        if mouse_row == 1:
            flag = 0
        else:
            flag = 1
        if flag == 1:
            mouse_row += 1
        else:
            pass

    elif mouse_col < cheese_col:
        mouse_col += 1
        if mouse_col == 1:
            flag = 0
        else:
            flag = 1
        if flag == 1:
            mouse_col -= 1
        else:
            pass

    elif mouse_col > cheese_col:
        mouse_col -= 1
        if mouse_col == 1:
            flag = 0
        else:
            flag = 1
        if flag == 1:
            mouse_col += 1
        else:
            pass

for i in range(n):
    for j in range(n):
        if (i, j) == (mouse_row, mouse_col):
            print(MOUSE, end="\t")
        elif (i, j) == (cheese_row, cheese_col):
            print(CHEESE, end="\t")
        else:
            print(MATRIX[i][j], end="\t")
    print()
