R, C, T = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(R)]

up = -1
down = -1

for i in range(R):
    if room[i][0] == -1:
        up = i
        down = i + 1
        break


def diffusion():
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    tmp_room = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if room[i][j] != -1 and room[i][j] != 0:
                tmp = 0
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx < R and 0 <= ny < C and room[nx][ny] != -1:
                        tmp_room[nx][ny] += room[i][j] // 5
                        tmp += room[i][j] // 5
                room[i][j] -= tmp
    for i in range(R):
        for j in range(C):
            room[i][j] += tmp_room[i][j]


def air_up():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direction = 0
    before = 0
    x, y = up, 1
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if x == up and y == 0:
            break
        if 0 > nx or nx >= R or ny < 0 or ny >= C:
            direction += 1
            continue
        room[x][y], before = before, room[x][y]
        x = nx
        y = ny


def air_down():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direction = 0
    before = 0
    x, y = down, 1
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if x == down and y == 0:
            break
        if 0 > nx or nx >= R or ny < 0 or ny >= C:
            direction += 1
            continue
        room[x][y], before = before, room[x][y]
        x = nx
        y = ny


for _ in range(T):
    diffusion()
    air_up()
    air_down()

ans = 0

for i in range(R):
    for j in range(C):
        if room[i][j] > 0:
            ans += room[i][j]

print(ans)
