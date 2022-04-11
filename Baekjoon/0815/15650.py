def go(index, cur_num, n, m):
    if index == m:
        print(*a)
        return
    for i in range(cur_num, n+1):
        if c[i]:
            continue
        c[i] = True
        a[index] = i
        go(index+1, i, n, m)
        c[i] = False

n, m = map(int, input().split())
c = [False] * (n + 1)
a = [0] * m


go(0, 1, n, m)