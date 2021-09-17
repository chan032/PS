n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))
# print(nums)
if n <= 3:
    if n == 1:
        print(nums[0])
    elif n == 2:
        print(sum(nums))
    else:
        print(max(nums[0] + nums[1], nums[0] + nums[2], nums[2] + nums[1]))
else:
    dpTable = [[0] * 2 for i in range(n + 1)]
    dpTable[1][1] = nums[0]
    dpTable[2][0] = nums[0]
    dpTable[2][1] = sum(nums[:2])
    dpTable[3][0] = sum(nums[:2])
    dpTable[3][1] = max(nums[0] + nums[1], nums[0] + nums[2], nums[1] + nums[2])

    for i in range(4, n + 1):
        dpTable[i][0] = max(dpTable[i - 1])
        dpTable[i][1] = max(max(dpTable[i - 2]) + nums[i - 1], max(dpTable[i - 3]) + nums[i - 1] + nums[i - 2])

    print(max(dpTable[n]))