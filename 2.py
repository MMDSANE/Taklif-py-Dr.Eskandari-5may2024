import random

matrix = []
for i in range(1 , 6):
    R = []
    
    for j in range(1 , 6):
        R.append(0)
    matrix.append(R)

for x in range(10):
    while True:
        R = random.randint(0, 4)
        C = random.randint(0, 4)
        if matrix[R][C] == 0:
            matrix[R][C] = 1
            break

for i in matrix:
    print(' '.join(map(str, i)))
