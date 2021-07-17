from collections import deque


def bfs(x, y):
    global count
    queue = deque()
    queue.append([x, y])

    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [-2, -1, 1, 2, -2, -1, 1, 2]
    if x == x1 and y == y1:
        return
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx == x1 and ny == y1:
                graph[nx][ny] = graph[x][y] + 1
                return
            if nx >= 0 and nx <= size -1 and ny >=0 and ny <= size - 1 and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])

totalCase = int(input())
answer = []
for c in range(totalCase):
    size = int(input())
    graph = [[0] * size for _ in range(size)]
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())


    count = 0
    bfs(x0, y0)
    answer.append(graph[x1][y1])

for i in answer:
    print(i)