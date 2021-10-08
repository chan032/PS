from collections import deque

n, m = map(int, input().split())  
nums = list(map(int, input().split()))
print(nums)


def check(mid):
    tmpList = deque(nums)
    
    for _ in range(m):
        if not tmpList:
            return True

        tmp = 0
        while True:
            if tmpList and (tmp + tmpList[0]) <= mid:
                tmp += tmpList.popleft()
            else:
                break

    if tmpList:
        return False
    else:
        return True

left = 0 # 불가능
right = int(1e9) # 가능
while True:
    if right - left == 1:
        break
    else:
        mid = (left + right) // 2

        if check(mid):
            right = mid
        else:
            left = mid

print(right)