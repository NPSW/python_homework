import numpy
import math


def harmonicSmall(n):
    res = 0.0
    for i in range(n):
        res += (1 / n)
    return res


def harmonicLarge(n):
    return math.log(n, math.exp(1)) + numpy.euler_gamma + (1 / (2 * n)) - (1 / (12 * (n**2))) - (1 / (120 * (n**4)))


def harmonic(n):
    if n < 100:
        return harmonicSmall(n)
    else:
        return harmonicLarge(n)


n = int(input())
print(harmonic(n))
