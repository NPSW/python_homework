

n = int(input())
m = int(input())
k = int(input())

if n < m:
    tmp = m
    m = n
    n = tmp

vn = 0
vm = 0

while True:
    vn = n
    print()
    print("1 сосуд:" + str(vn))
    print("2 сосуд:" + str(vm))
    while True:
        s = min(m - vm, vn)
        vm += s
        vn -= s
        print()
        print("1 сосуд:" + str(vn))
        print("2 сосуд:" + str(vm))

        if vm >= m:
            vm = 0
            print()
            print("1 сосуд:" + str(vn))
            print("2 сосуд:" + str(vm))

        if vn == k:
            break
        if vm != m and vm != 0:
            break
        if vn == 0:
            break

    if vn == k:
        break
