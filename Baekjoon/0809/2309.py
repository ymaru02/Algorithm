# 2309 일곱 난쟁이

result = []
for _ in range(9):
    result.append(int(input()))

gap = sum(result) - 100
result.sort()

breaker = False
for i in result:
    for j in result:
        if gap == i + j:
            result.remove(i)
            result.remove(j)
            breaker = True
            break
    if breaker:
        break

for i in result:
    print(i)