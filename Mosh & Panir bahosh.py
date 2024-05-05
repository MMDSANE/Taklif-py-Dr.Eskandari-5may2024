import random  # AVAZ SHODAN JAYE MOOSH VA PANIR

# ANASOR MAZE
MOUSE = "\U0001F401"
CHEESE = "\U0001F9C0"

n = 10
MATRIX = []
num = n ** 2

mouse_row = random.randint(1, n - 2)
mouse_col = random.randint(1, n - 2)

cheese_row = random.randint(1, n - 2)
cheese_col = random.randint(1, n - 2)

for i in range(n): 
    row = []
    for j in range(num):
        if i == 0 or j == 0 or i == n-1 or j == n-1:
            row.append(0)
        else:
            row.append(random.randint(0 , 1))

            if i == 4 and j == 5:
                row[j] = MOUSE
            if i ==8 and j == 8:
                row[j] = CHEESE
    MATRIX.append(row)



for i in range(n):
    for j in range(n):
        print(f"{MATRIX[i][j]}" , end="\t")
    print()
print("\n , \n")

while (MOUSE, CHEESE) != (MOUSE, CHEESE):
    if MOUSE < CHEESE:
        MOUSE += 1
    elif MOUSE > CHEESE:
        MOUSE -= 1
    elif MOUSE < CHEESE:
        MOUSE += 1
    elif MOUSE > CHEESE:
        MOUSE -= 1

for i in range(n):
    for j in range(n):
        if (i, j) == (MOUSE):
            print(MOUSE, end="\t")
        elif (i, j) == (CHEESE):
            print(CHEESE, end="\t")
        else:
            print(MATRIX[i][j], end="\t")
    print()
