from collections import deque

dx = [0, 0, 0, 1, -1]
dy = [0, 1, -1, 0, 0]


def bfs(x, y):
    q = deque([(x, y)])
    s = 0
    w = 0
    while q:
        x, y = q.popleft()
        for d in range(5):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                if graph[nx][ny] == "#":
                    continue
                elif graph[nx][ny] == "v":
                    w += 1
                elif graph[nx][ny] == "o":
                    s += 1
                q.append([nx, ny])
                visited[nx][ny] = True
    return s, w


R, C = map(int, input().split())

graph = []
visited = [[False] * C for _ in range(R)]

양, 늑대 = 0, 0

for _ in range(R):
    graph.append(list(input().rstrip()))

for i in range(R):
    for j in range(C):
        if not visited[i][j] and graph[i][j] != '#':
            s, w = bfs(i, j)
            if s > w:
                양 += s
            else:
                늑대 += w

print(양, 늑대)
