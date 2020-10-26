import numpy
import math
import random


def evaluate(x, a, count):
    if count == n - 1:
        return a[count - 1]

    return a[count] + (x * evaluate(x, a, count + 1))


def exp(x):
    exp_arr = [0.0 for i in range(n)]
    for i in range(n):
        exp_arr[i] = 1 / (math.factorial(i))

    return evaluate(x, exp_arr, 0)


n = 30
arr = [random.randint(-5, 5) for i in range(n)]
q = int(input())
print(evaluate(q, arr, 0))
print(exp(q))
print(math.exp(q))
