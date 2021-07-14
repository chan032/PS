import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())

graph = [[] for i in range(n + 1)]
# graph = {i : [] for i in range(1, n + 1)}
for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

distance = [INF for i in range(n + 1)]
# distance = {i : INF for i in range(1, n + 1)}


def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start)) # min heap
    distance[start] = 0

    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue
            
        for b, c in graph[now]:
            cost = dist + c
            if cost < distance[b]:
                distance[b] = cost
                heapq.heappush(heap, (cost, b))

dijkstra(start)
count = 0
max_distance = 0
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

print(count - 1, max_distance)