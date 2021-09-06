totalCase = int(input())
numList = []
for c in range(totalCase):
    numList.append(int(input()))


dpTable = [[0] * 3 for i in range(max(numList) + 1)]
dpTable[1][0] = 1
dpTable[2][1] = 1
dpTable[3][0] = 1
dpTable[3][1] = 1
dpTable[3][2] = 1

for i in range(4, max(numList) + 1):
    dpTable[i][0] = (dpTable[i - 1][1] + dpTable[i - 1][2]) % 1000000009
    dpTable[i][1] = (dpTable[i - 2][0] + dpTable[i - 2][2]) % 1000000009
    dpTable[i][2] = (dpTable[i - 3][0] + dpTable[i - 3][1]) % 1000000009

for i in numList:    
    print(sum(dpTable[i]) % 1000000009)

