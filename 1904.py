MOD = 15746

n = int(input())

if n < 3:
    print(n)
else:
    dpTable = [0 for i in range(n + 1)]
    dpTable[1] = 1
    dpTable[2] = 2
    for i in range(3, n + 1):
        dpTable[i] = (dpTable[i - 1] + dpTable[i - 2]) % MOD

    print(dpTable[-1])