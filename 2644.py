from collections import deque

n = int(input())
x, y = map(int, input().split())
m = int(input())
graph = {i : [] for i in range(1, n + 1)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start, target):
    global n

    queue = deque([start])
    distance = [0] * (n + 1)

    while queue:
        n = queue.popleft()
        for m in graph[n]:
            if distance[m] == 0 or distance[n] + 1 < distance[m]:
                distance[m] = distance[n] + 1
                queue.append(m)        
            
    return distance[target]

answer = bfs(x, y)
if answer == 0:
    print(-1)
else:
    print(answer)