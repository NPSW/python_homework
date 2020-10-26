import math

for i in range(1, 150):
    for j in range(1, 150):
        if j > i:
            break

        for a in range(1, 150):
            if a > j:
                break

            for b in range(1, 200):
                if b > a:
                    break

                m = (i**5) + (j**5) + (a**5) + (b**5)
                m = m**(1/5)
                if (m - int(m)) < 0.0000000000001:
                    print(m**5)
                    print(i)
