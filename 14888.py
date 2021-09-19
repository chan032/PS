from itertools import permutations

n = int(input())
nums = list(map(int, input().split()))
counts = list(map(int, input().split()))
opers = []
for i in range(4):
    if counts[i] == 0:
        continue
    else:
        for _ in range(counts[i]):
            opers.append(i)
# print(opers)
# print(opers)

MAX = -int(1e10)
MIN = int(1e10)
cases = set(permutations(opers, n - 1))
for case in cases:
    i = 0
    tmp = nums[i]
    for c in case:
        i += 1
        if c == 0:
            tmp += nums[i]
        elif c == 1:
            tmp -= nums[i]
        elif c == 2:
            tmp *= nums[i]
        else:  # c == 3:
            if tmp < 0 and nums[i] > 0:
                tmp *= -1
                tmp //= nums[i]
                tmp *= -1
            else:
                tmp //= nums[i]
    # print(case)
    # print(tmp)
    MAX = max(tmp, MAX)
    MIN = min(tmp, MIN)

print(MAX)
print(MIN)