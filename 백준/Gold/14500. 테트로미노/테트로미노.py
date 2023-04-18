N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 최대값
max_value = max(map(max, board))

ans = 0


def dfs(x, y, tmp_ans, block):
    # 전역 변수
    global ans
    # 아무리해도 정답보다 작을 경우
    if tmp_ans + max_value * (4 - block) <= ans:
        return

    # 블록 종류별로 다 썻을때
    if block == 4:
        ans = max(ans, tmp_ans)
        return
    # dfs 시작
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            # ㅗ 모양 때문에 두번째에서 모양 변형 탐색
            if block == 2:
                visited[nx][ny] = True
                dfs(x, y, tmp_ans + board[nx][ny], block + 1)
                visited[nx][ny] = False

            visited[nx][ny] = True
            dfs(nx, ny, tmp_ans + board[nx][ny], block + 1)
            visited[nx][ny] = False


for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, board[i][j], 1)
        visited[i][j] = False

print(ans)
