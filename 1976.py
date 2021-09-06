def findParent(parent, x):
    # if parent[x] != x:
    #     parent[x] = findParent(parent, parent[x])
    # else:
    #     return parent[x] -> typeError

    ####test
    # if parent[x] == x:
    #     return x
    # return findParent(parent, parent[x])
    if parent[x] != x:
        parent[x] = findParent(parent, parent[x])
    
    return parent[x]
    

def union(parent, x1, x2):
    parent1 = findParent(parent, x1)
    parent2 = findParent(parent, x2)

    if parent1 != parent2:
        parent[min(parent1, parent2)] = max(parent1, parent2)

n = int(input())
parentList = [i for i in range(n + 1)]
m = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))        
for i in range(1, n):
    for j in range(i):
        if graph[i][j] == 1:
            union(parentList, i + 1, j + 1)
mList = map(int, input().split())
answer = []
for i in mList:
    answer.append(findParent(parentList, i))

if len(set(answer)) == 1:
    print("YES")
else:
    print("NO")