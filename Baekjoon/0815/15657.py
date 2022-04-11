def go(index, cur_num, num_list, n, m):
    if index == m:
        print(*a)
        return
    for i in range(cur_num, n):
        # if c[i]: 
        #     continue
        c[i] = True
        a[index] = num_list[i]
        go(index+1, i, num_list, n, m)
        c[i] = False

n, m = map(int, input().split())
number_list = list(map(int, input().split()))
c = [False] * n 
a = [0] * m
number_list.sort()

go(0, 0, number_list, n, m)