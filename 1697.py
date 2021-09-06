from collections import deque

n, k = map(int, input().split())
visited = [False] * 100001
countList = [0] * 100001


count = 0
def bfs(start, target):
    queue = deque([])
    queue.append(start)

    while queue:
        x = queue.popleft()
        # print(x)
        if x == target:
            return 

        if not visited[x]:
            visited[x] = True
            dx = [-1, 1, x]
            for i in range(3):
                nx = x + dx[i]
                if nx >= 0 and nx <= 100000 and countList[nx] == 0:
                    queue.append(nx)
                    # print(nx)
                    countList[nx] = countList[x] + 1

bfs(n, k)
print(countList[k])
