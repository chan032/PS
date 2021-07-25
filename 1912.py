import sys
input = sys.stdin.readline

total = int(input())  # [1, 10 0000]
numList = list(map(int, input().split()))


dpTable = [[0] * (total + 1) for i in range(2)]
dpTable[1][1] = numList[0]
for i in range(2, total + 1):
    dpTable[1][i] = max(numList[i - 1], numList[i - 1] + dpTable[1][i - 1])
    dpTable[0][i] = max(dpTable[1][1:i]) 

print(max(dpTable[0][total], dpTable[1][total]))