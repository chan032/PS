import sys

n = int(input())
totalLen = len(str(n))


if totalLen == 1:
    print(n)
else:
    answer = 0
    for i in range(1, totalLen):
        if i == 1:
            answer += 9
        else:
            answer += 9 * (10**(i - 1)) * i

    answer += (n - (10**(totalLen - 1)) + 1) * totalLen

    print(answer)
        