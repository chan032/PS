totalCase = int(input())
for _ in range(totalCase):
    v, e = map(int, input().split())
    parentList = [i for i in range(v + 1)]


    def findParent(parent, x):
        if parent[x] != x:
            parent[x] = findParent(parent, parent[x])
        return parent[x]

    def union(parent, a, b):
        parent1 = findParent(parent, a)
        parent2 = findParent(parent, b)

        if parent1 == parent2:
            return        

        parent[min(parent1, parent2)] = max(parent1, parent2)

    for i in range(e):
        a, b = map(int, input().split())
        union(parentList, a, b)
    answer = []
    for i in range(1, v + 1):
        answer.append(findParent(parentList, i))
    print(answer)
    if len(set(answer)) == 1:
        print("YES")
    else:
        print("NO")