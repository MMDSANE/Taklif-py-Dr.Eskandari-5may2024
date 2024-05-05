import random

MATRIX = []
for i in range(6):
    row = []
    for j in range(6):
        row.append(0)
    MATRIX.append(row)

num_random = 12

for i in range(num_random):
    row = random.randint(0, 5)
    col = random.randint(0, 5)
    MATRIX[row][col] = random.randint(1, 9)

for row in MATRIX:
    print(row)
