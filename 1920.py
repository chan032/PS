total1 = int(input())
numList1 = list(map(int, input().split()))
numList1.sort()
total2 = int(input())
numList2 = list(map(int, input().split()))


def searchNumber(numList, target, start, end):
    if start > end:
        return 0
        
    mid = (start + end) // 2
    if numList[mid] == target:
        return 1
    elif target < numList[mid]:
        return searchNumber(numList, target, start, mid - 1)
    else: 
        return searchNumber(numList, target, mid + 1, end)


for i in numList2:
    print(searchNumber(numList1, i, 0, total1 - 1))