from collections import deque

total = int(input())
numQue = deque(map(int, input().split()))

operList = list(map(int, input().split()))  



answerMax = int(-1e10)
answerMin = int(1e10)
def dfs(que):
    x0 = que.popleft()

    for 
    for i in range(4):
        if operList[i] <= 0:
            continue

        if i == 0:
            pass
        elif i == 1:
            pass
        elif i == 2:
            pass
        else:
            pass

dfs(numQue)
print(answerMax, answerMin)