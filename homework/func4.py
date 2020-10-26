import math


def f(n, k, p):
    return math.log((p**k) * (p**(n - k)) * (math.factorial(n) / (math.factorial(k) * math.factorial(n - k))), math.exp(1))


n = int(input())
k = int(input())
p = float(input())

print(math.exp(f(n, k, p)))

sum = 0

for i in range(n + 1):
    sum += math.exp(f(n, i, p))

print(sum)
