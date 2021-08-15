total = int(input())
numList = list(map(int, input().split()))


if total <= 2:
    if total == 1:
        print(numList[0])
    else:
        print(max(numList[0], numList[1], sum(numList)))

else:
    dpTable = [[-1001] * total for _ in range(2)]
    dpTable[1][0] = numList[0]
    dpTable[1][1] = max(numList[1], numList[0] + numList[1])
    dpTable[0][1] = numList[0]


    for i in range(2, total):
        dpTable[1][i] = max(dpTable[1][i - 1], 0) + numList[i]
        dpTable[0][i] = max(dpTable[0][i - 1], dpTable[1][i - 1])
        # for j in range(i):
            # dpTable[0][i] = max(dpTable[1][:i])

    print(max(dpTable[0][total - 1], dpTable[1][total - 1]))
        