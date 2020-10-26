import random

a = [0] * 500
days = [0] * 365
flag = False

for i in range(500):
    flag = False
    for k in range(365):
        if flag:
            break
        r = random.randint(0, 364)
        days[r] += 1
        for j in range(365):
            if days[j] > 1:
                a[i] = k
                days = [0] * 365
                flag = True
                break

avg = 0

for i in range(500):
    avg += a[i]

print(avg / 500)
