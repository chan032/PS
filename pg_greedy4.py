def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x : x[2])
    # print(costs)
    
    parent = [i for i in range(n)]
    def find(parent, x):
        if x == parent[x]:
            return x
        else:
            parent[x] = find(parent, parent[x])
        
        return parent[x]
    
    def union(parent, x, y):
        x = find(parent, x)
        y = find(parent, y)
        
        if x < y:
            parent[y] = x
        else:
            parent[x] = y
    
    
    for a, b, cost in costs:
        if find(parent, a) == find(parent, b):
            continue
        else:
            answer += cost
            union(parent, a, b)
        
    return answer