from collections import deque

f, s, g, u, d = map(int, input().split())
d *= -1

visited = [0] * (f + 1)
def bfs(start):
    queue = deque([start])

    dx = [u, d]
    while queue:
        x = queue.popleft()
        if x == g:
            return True
        
        #x != g
        for i in range(2):
            if dx[i] == 0:
                continue
            nx = x + dx[i]
            if 1 <= nx <= f:
                if visited[nx] == 0 or visited[nx] > visited[x] + 1:
                    visited[nx] = visited[x] + 1
                    queue.append(nx)

    return False


if bfs(s):
    print(visited[g])
else:
    print("use the stairs")