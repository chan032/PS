INF = int(1e7)

n = int(input())  # [3, 5000]

if n <= 5:
    if n == 3 or n == 5:
        print(1)
    else:
        print(-1)
else:
    dpTable = [INF for i in range(n + 1)]
    dpTable[3] = 1
    dpTable[5] = 1
    for i in range(6, n + 1):
        dpTable[i] = min(dpTable[i - 3], dpTable[i - 5]) + 1

    answer = dpTable[n]
    if answer >= INF:
        print(-1)
    else:
        print(answer)
