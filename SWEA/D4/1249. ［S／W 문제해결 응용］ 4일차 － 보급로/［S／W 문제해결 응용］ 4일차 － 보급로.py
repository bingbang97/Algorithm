from collections import deque


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def road(arr):
    D[0][0] = 0
    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                if D[nx][ny] > D[x][y] + arr[x][y]:
                    D[nx][ny] = D[x][y] + arr[x][y]
                    q.append((nx, ny))

    return D[N - 1][N - 1]


T = int(input())
for tc in range(T):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]

    D = [[1e9] * N for _ in range(N)]

    ans = road(board)

    print(f'#{tc + 1} {ans}')