import random


prob_one = 0
prob_two = 0

count = 0

for i in range(10000):
    count = 0
    for j in range(6):
        r = random.randint(1, 6)
        if r == 1:
            count += 1

    if count == 1:
        prob_one += 1

    count = 0
    for o in range(12):
        r = random.randint(1, 6)
        if r == 1:
            count += 1

    if count == 2:
        prob_two += 1


print(prob_one / 10000)

print(prob_two / 10000)
