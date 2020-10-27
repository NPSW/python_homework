import itertools


def comb(s, m):
    return list(itertools.combinations(s, m))


n = int(input())

el = 'a'

alph = {el}

for i in range(1, n):
    alph.add(chr(ord(el) + i))

print("('',)")

for i in range(1, n + 1):
    res = comb(alph, i)

    for j in res:
        print(j)
