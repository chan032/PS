import sys
import math
input = sys.stdin.readline

numList = []
while True:
    n = int(input())  # [1, 12 3456]
    if n == 0:
        break

    numList.append(n)

maxNum = (2 * max(numList)) + 1
primeList = [True] * (maxNum + 1) 
for i in range(2, maxNum):
    if primeList[i]:
        cnt = 2
        while (i * cnt) <= maxNum:
            primeList[i * cnt] = False
            cnt += 1

for i in numList:
    cnt = 0
    for j in range(i + 1, (2 * i) + 1):
        if primeList[j]:
            cnt += 1
    
    print(cnt)
    





