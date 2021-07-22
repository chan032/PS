total = int(input())
numList = list(map(int, input().split()))

answer = numList[0] * numList[-1]
print(answer)