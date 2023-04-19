from collections import deque

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]
road = [[0] * C for _ in range(R)]

cnt = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

queue = deque()

end = []

for i in range(R):
    for j in range(C):
        if board[i][j] == 'S':
            queue.append([i, j])
        elif board[i][j] == 'D':
            end = [i, j]

for i in range(R):
    for j in range(C):
        if board[i][j] == '*':
            queue.append([i, j])


def bfs(arr):
    while queue:
        x, y = queue.popleft()
        if [x, y] == arr:
            return (road[x][y])
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if (board[nx][ny] == 'D' or board[nx][ny] == '.') and board[x][y] == 'S':
                    board[nx][ny] = 'S'
                    road[nx][ny] = road[x][y] + 1
                    queue.append([nx, ny])
                elif (board[nx][ny] == 'S' or board[nx][ny] == '.') and board[x][y] == '*':
                    board[nx][ny] = '*'
                    queue.append([nx, ny])

    return ('KAKTUS')


print(bfs(end))
