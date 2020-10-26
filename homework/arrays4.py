import os
import random


def maze_init():
    for i in range(n):
        for j in range(m):
            maze[i + 1][j + 1] = random.randint(0, 1)


def count(x, y, col):
    if col[0][x][y]:
        return [0, 10000000]
    if maze[x][y] == 1:
        return [0, 10000000]

    col[1] += 1
    col[0][x][y] = 1

    if (maze[x][y + 1] == -1) or (maze[x][y - 1] == -1) or (maze[x + 1][y] == -1) or (maze[x - 1][y] == -1):
        return col

    top = [0, 10000000]
    bot = [0, 10000000]
    left = [0, 10000000]
    right = [0, 10000000]

    if (maze[x][y] == maze[x][y + 1]) and (not col[0][x][y + 1]):
        bot = count(x, y + 1, col)
    if (maze[x][y] == maze[x + 1][y]) and (not col[0][x + 1][y]):
        right = count(x + 1, y, col)
    if (maze[x][y] == maze[x][y - 1]) and (not col[0][x][y - 1]):
        top = count(x, y - 1, col)
    if (maze[x][y] == maze[x - 1][y]) and (not col[0][x - 1][y]):
        left = count(x - 1, y, col)

    mm = min(top[1], bot[1], right[1], left[1])
    if mm == top:
        return top
    if mm == bot:
        return bot
    if mm == right:
        return right
    if mm == left:
        return left


n = 20
m = 20
maze = [[-1] * (m + 2) for i in range(n + 2)]
colors = [[0] * (m + 2) for j in range(n + 2)]
colors = [colors, 0]

for i in range(n):
    for j in range(m):
        maze[i + 1][j + 1] = 0

while True:
    maze_init()
    stx = 0
    sty = 0
    flag = False

    while True:
        stx = random.randint(1, n + 1)
        sty = random.randint(1, m + 1)
        if maze[stx][sty] == 0:
            maze[stx][sty] = 2
            break

    if count(stx, sty, colors)[1] < 100000:
        break

for i in range(n):
    print()
    for j in maze[i + 1][1:m + 1]:
        print(j, end=" ")

print()
for i in range(n):
    print()
    for j in colors[0][i + 1][1:m + 1]:
        print(j, end=" ")

print()
print(stx)
print(sty)
