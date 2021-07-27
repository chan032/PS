import sys
input = sys.stdin.readline

total = int(input())  # [1, 10 0000]
numList = []
for i in range(total):
    numList.append(int(input()))
numList.sort()


answer = 0
for i in range(len(numList)):
    totalRest = len(numList) - i
    totalSum = totalRest * numList[i]

    answer = max(answer, totalSum)

print(answer)






