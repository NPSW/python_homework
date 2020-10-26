import random

n = int(input())
prob_nothing = 0
prob_change = 0

for i in range(n):
    prize = random.randint(1, 3)
    choice = random.randint(1, 3)

    if prize != choice:
        option = prize
    else:
        if prize == 1:
            option = 2
        if prize == 2:
            option = 3
        if prize == 3:
            option = 1

    if choice == prize:
        prob_nothing += 1
    else:
        prob_change += 1


print(prob_nothing / n)
print(prob_change / n)
