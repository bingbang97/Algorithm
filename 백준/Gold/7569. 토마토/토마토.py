from collections import deque


def bfs(graph, tomato):
    count = 0
    while tomato:
        for _ in range(len(tomato)):
            x, y, z = tomato.popleft()
            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]
                if nx < 0 or ny < 0 or nz < 0 or nx >= n or ny >= m or nz >= h:
                    continue
                if graph[nz][nx][ny] == 0:
                    graph[nz][nx][ny] = 1
                    tomato.append((nx, ny, nz))
        count += 1
    return count

m, n, h = map(int, input().split())
graph = [[[0] * m for _ in range(n)] for _ in range(h)]
tomato = deque()

for k in range(h):
    for i in range(n):
        inputData = list(map(int, input().split()))
        for j in range(m):
            graph[k][i][j] = inputData[j]
            if graph[k][i][j] == 1:
                tomato.append((i, j, k))

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

day = bfs(graph, tomato)
numOfZero = 0

for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 0:
                numOfZero += 1

if numOfZero == 0:
    print(day - 1)
else:
    print(-1)