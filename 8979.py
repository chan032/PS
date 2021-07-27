n, k = map(int, input().split()) # n : [1, 1000]
infoList = []
for i in range(1, n + 1):
    infoList.append(list(map(int, input().split())))



infoList = sorted(infoList, key = lambda x : (-x[1], -x[2], -x[3]))
print(infoList) 
