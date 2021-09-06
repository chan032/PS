total = int(input())
numList = list(map(int, input().split()))
numList.sort()


p1 = 0
p2 = total - 1
answer = 9876543210
while p1 < p2:
    mix = abs(numList[p1] + numList[p2])
    #p1 up case
    #p2 down case