import math


def euler(n):
    if n == 1:
        return 1
    count = 0
    i = 2
    while i < n:
        for j in range(2, i + 1):
            if (i % j == 0) and (n % j == 0):
                count += 1
                break
        i += 1

    return n - count - 1


q = int(input())
print(euler(q))
