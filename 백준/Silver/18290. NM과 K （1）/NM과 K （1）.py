N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
answer = -int(1e9)

def dfs(px, py, idx, sum):
    if idx == K:
        global answer

        if answer < sum:
            answer = sum
        return

    for x in range(px, N):
        for y in range(py if x == px else 0, M):
            # 현재 위치 방문했었는지 확인
            if visited[x][y]:
                continue
            tmp = True
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    if visited[nx][ny]:
                        tmp = False
            if tmp:
                visited[x][y] = True
                dfs(x, y, idx + 1, sum + arr[x][y])
                visited[x][y] = False

dfs(0, 0, 0, 0)

print(answer)