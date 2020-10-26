import math

n = int(input())
used = set()

for i in range(1, int(math.pow(n, 1/3)) + 1):
    for j in range(1, int(math.pow(n, 1/3)) + 1):
        if i**3 + j**3 > n:
            pass
        for a in range(1, int(math.pow(n, 1/3)) + 1):
            for b in range(1, int(math.pow(n, 1/3)) + 1):
                if a**3 + b**3 > n:
                    pass
                elif (a**3 + b**3 == i**3 + j**3) and (a != i) and (a != j):
                    if not (a**3 + b**3) in used:
                        print(a**3 + b**3)
                        used.add(a**3 + b**3)

