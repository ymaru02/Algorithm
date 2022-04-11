N = input()

num = int(N)
num_len = len(N)
result = (num - (10 ** (num_len - 1)) + 1) * num_len
for i in range(1, num_len):
    result += 10 ** (i - 1) * 9 * (i)
print(result)

# =======================================================
n = int(input())
ans = 0
start = 1
length = 1
while start <= n:
    end = start*10-1
    if end > n:
        end = n
    ans += (end-start+1)*length
    start *= 10
    length += 1
print(ans)