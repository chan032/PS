n, s = map(int, input().split())
nums = list(map(int, input().split()))
# print(nums)

count = 0
curSum = 0
def dfs(start):
    global count 
    global curSum 

    if start == n:
        return
    else:
        if (curSum + nums[start]) == s:
            count += 1

        dfs(start + 1)

        curSum += nums[start]
        dfs(start + 1)

        curSum -= nums[start]

dfs(0)
print(count)
