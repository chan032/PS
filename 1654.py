k, n = map(int, input().split())
nums = []
for i in range(k):
    nums.append(int(input()))
nums.sort()
# print(nums)


def check(mid):
    tmp = 0
    for num in nums:
        tmp += num // mid

    if tmp >= n:
        return True
    else:
        return False


left = 1  # 만족
right =  max(nums) + 1
while True:
    if left + 1 == right:
        break
    else:
        mid = (left + right) //2

        if check(mid):
            left = mid
        else:
            right = mid

print(left)
