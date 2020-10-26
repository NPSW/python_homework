import random

n= int(input())
m = int(input())
p = float(input())

arr = [[-2] * (m + 2) for i in range(n + 2)]


for i in range(n):
    for j in range(m):
        r = random.randint(0, 100)
        if r < (p * 100):
            arr[i + 1][j + 1] = -1
        else:
            arr[i + 1][j + 1] = 0


for i in range(n):
    for j in range(m):
        if arr[i + 1][j + 1] == -1:
            continue
        elif arr[i + 1][j + 1] == 0:
            if arr[i][j] == -1:
                arr[i + 1][j + 1] += 1
            if arr[i][j + 1] == -1:
                arr[i + 1][j + 1] += 1
            if arr[i][j + 2] == -1:
                arr[i + 1][j + 1] += 1
            if arr[i + 1][j] == -1:
                arr[i + 1][j + 1] += 1
            if arr[i + 1][j + 2] == -1:
                arr[i + 1][j + 1] += 1
            if arr[i + 2][j] == -1:
                arr[i + 1][j + 1] += 1
            if arr[i + 2][j + 1] == -1:
                arr[i + 1][j + 1] += 1
            if arr[i + 2][j + 2] == -1:
                arr[i + 1][j + 1] += 1


for i in range(n):
    print()
    for j in arr[i + 1][1:m + 1]:
        if j == -1:
            print('*', end=" ")
        elif j == 0:
            print('.', end=" ")
        else:
            print(j, end=" ")



#for i in range(n):
#    for j in range(m):
#        if arr[i + 1][j + 1] == -1:
#            arr[i + 1][j + 1] = '*'
#        elif arr[i + 1][j + 1] == 0:
#            arr[i + 1][j + 1] = '.'

#for i in range(n + 2):
#    print(arr[i + 1][1:m + 1])

