import sys
input = sys.stdin.readline

n = int(input()) # [1, 50 0000]
nList = list(map(int, input().split()))
nDict = dict()
for i in nList:
    nDict.setdefault(i, None)
m = int(input())
mList = list(map(int, input().split()))


answer = []
for i in mList:
    if i in nDict.keys():
        answer.append('1')
    else:
        answer.append('0')

print(' '.join(answer))
        

    