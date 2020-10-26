import random


def count(x, y):
    if colors[x][y]:
        return 0

    colors[x][y] = 1
    top = 0
    bot = 0
    left = 0
    right = 0

    if (arr[x][y] == arr[x][y + 1]) and (not colors[x][y + 1]):
        bot = count(x, y + 1)
    if (arr[x][y] == arr[x + 1][y]) and (not colors[x + 1][y]):
        right = count(x + 1, y)
    if (arr[x][y] == arr[x][y - 1]) and (not colors[x][y - 1]):
        top = count(x, y - 1)
    if (arr[x][y] == arr[x - 1][y]) and (not colors[x - 1][y]):
        left = count(x - 1, y)

    return 1 + top + left + bot + right


n = int(input())
m = int(input())
numb = int(input())

arr = [[-1] * (m + 2) for i in range(n + 2)]

for i in range(n):
    for j in range(m):
        arr[i + 1][j + 1] = random.randint(0, numb - 1)

colors = [[0] * (m + 2) for i in range(n + 2)]

for i in range(n):
    print()
    for j in arr[i + 1][1:m + 1]:
        print(j, end=" ")

max_path = 0
max_number = -1

for i in range(n):
    for j in range(m):
        a = count(i + 1, j + 1)
        if max_path < a:
            max_path = a
            max_number = arr[i + 1][j + 1]

print()
print(max_path)
print(max_number)
