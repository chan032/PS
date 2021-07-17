total = int(input())
rgbList = []
for i in range(total):
    rgbList.append(list(map(int, input().split())))
    
dpTable = [[1001] * 3 for i in range(total)]
dpTable[0][0] = rgbList[0][0]
dpTable[0][1] = rgbList[0][1]
dpTable[0][2] = rgbList[0][2]


for i in range(1, total):
    dpTable[i][0] = min(dpTable[i - 1][1], dpTable[i - 1][2]) + rgbList[i][0]
    dpTable[i][1] = min(dpTable[i - 1][0], dpTable[i - 1][2]) + rgbList[i][1]
    dpTable[i][2] = min(dpTable[i - 1][1], dpTable[i - 1][0]) + rgbList[i][2]

print(min(dpTable[total - 1]))