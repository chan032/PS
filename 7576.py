import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))


def bfs(x, y):
    queue = deque()
    queue.append([x, y])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if n > nx >= 0 and m > ny >= 0:
                if graph[nx][ny] == -1:
                    continue
                if graph[nx][ny] == 0 or graph[x][y] + 1 < graph[nx][ny]:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append([nx, ny])



for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            bfs(i, j)

answer = 0
for i in graph:
    if 0 in i:
        answer = 0
        break
    else:
        answer = max(answer, max(i))

print(answer - 1)