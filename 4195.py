def findParent(parent, x):
    if parent[x] != x:
        parent[x] = findParent(parent, parent[x])
    return parent[x]

def union(x1, x2):
    p1 = findParent(parent, x1)
    p2 = findParent(parent, x2)

    if p1 < p2:
        parent[p2] = p1
    else:
        parent[p1] = p2

totalLink = int(input())
parent = [i for i in range(totalLink)]
nameDict = dict()
for i in range(totalLink):
    nameKey = 0
    name1, name2 = input().split()
    if name1 not in nameDict.keys():
        nameDict.setdefault(name1, nameKey)
        nameKey += 1
    if name2 not in nameDict.keys():
        nameDict.setdefault(name2, nameKey)
        nameKey += 1
    
    union(nameDict[name1], nameDict[name2])
    root = findParent(parent, nameDict[name1])
    count = 0
    for j in parent:
        if root  == j:
            count += 1
    print(count)


