T = int(input())

cnt = 0
for i in range(T):
    N = map(int, input().split())    
    is_prim = True    
    if N < 2:
        is_prim = False
    for j in range(2, int(N ** 0.5 + 1)):
        if not N % 2:
            is_prim = False
    if is_prim:
        cnt += 1
print(cnt)