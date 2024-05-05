from random import shuffle , randint

matrix = []
n = 9
num = n ** 2

for x in range(n):
    row = []
    for y in range(1 , num):
        z = randint(1 , 9)
        
        row.append(z)
    
    matrix.append(row)
#print(matrix)

for i in range(n):
    for j in range(n):
        print(f"{matrix[i][j]:4}" , end='')
    print()