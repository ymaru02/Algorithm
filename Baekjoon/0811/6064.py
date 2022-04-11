T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    x -= 1
    y -= 1
    i = x

    while i < N*M:
        if i % N == y:
            print(i+1)
            break
        i += M
    else:
        print(-1)


# =======================================================
t = int(input())

for _ in range(t):
    m,n,x,y = map(int,input().split())
    x -= 1
    y -= 1
    k = x
    while k < n*m:
        if k%n == y:
            print(k+1)
            break
        k += m
    else:
        print(-1)