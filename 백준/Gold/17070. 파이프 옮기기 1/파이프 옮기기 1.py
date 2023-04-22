def dfs(x, y, d):
    # d = 방향 (가로 : 0, 세로 : 1, 대각선 : 2)
    global ans
    nx = x + 1
    ny = y + 1
    if nx == N and ny == N:
        ans += 1
        return
    if d == 0 or d == 2:
        if ny < N:
            if arr[x][ny] == 0:
                dfs(x, ny, 0)
    if d == 1 or d == 2:
        if nx < N:
            if arr[nx][y] == 0:
                dfs(nx, y, 1)

    if d == 0 or d == 1 or d == 2:
        if nx < N and ny < N:
            if arr[nx][y] == 0 and arr[x][ny] == 0 and arr[nx][ny] == 0:
                dfs(nx, ny, 2)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
dfs(0, 1, 0)
print(ans)
