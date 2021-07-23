MOD = int(1e9)

n, k = map(int, input().split())


dpTable = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dpTable[i][1] = 1
for i in range(1, k + 1):
    dpTable[1][i] = i

# for j in range(2, k + 1):
#     for i in range(2, n + 1):
#         tmp = 0
#         for a in range(0, n):
#             tmp += dpTable[i - a][j - 1]
        
#         dpTable[i][j] = (tmp + 1) % MOD
for i in range(2, n + 1):
    for j in range(2, k + 1):
        dpTable[i][j] = (dpTable[i - 1][j] + dpTable[i][j - 1]) % MOD


# print(dpTable)
print(dpTable[n][k])
