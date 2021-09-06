total = int(input())
numList = list(map(int, input().split()))
numList.sort()
x = int(input())


count = 0
for p1 in range(total - 1):
    p2 = p1 + 1
    if p1 == total - 2:
        if numList[p1] + numList[p2] == x:
            count += 1
        else:
            break
    if numList[p1] + numList[p2] > x:
        continue
    elif numList[p1] + numList[p2] == x:
        count += 1
        continue
    while p2 <= total - 1:
        if numList[p1] + numList[p2] > x:
            break
        if numList[p1] + numList[p2] == x:
            count += 1
            break
        p2 += 1

print(count)