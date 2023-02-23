import sys


def sudoku(y, x):
    num_list = list(range(1, 10))
    tmp = []
    for k in range(9):
        if arr[y][k] != 0:
            tmp.append(arr[y][k])
        if arr[k][x] != 0:
            tmp.append(arr[k][x])
    # 가로 세로 탐색
    x = (x // 3) * 3
    y = (y // 3) * 3
    for dy in range(y, y + 3):
        for dx in range(x, x + 3):
            if arr[dy][dx] != 0:
                tmp.append(arr[dy][dx])
    # 박스 검사
    tmp = set(tmp)
    num_list = list(set(num_list) - tmp)
    return num_list
    # 가능한 숫자 리스트 리턴


def dfs(cnt):
    if cnt == len(zero_list):
        for n in range(N):
            print(*arr[n])
        exit(0)
    else:
        (y, x) = zero_list[cnt]
        num = sudoku(y, x)
        for k in num:
            arr[y][x] = k
            dfs(cnt + 1)
            arr[y][x] = 0
        # 숫자 넣고 dfs 반복


N = 9
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
zero_list = [(i, j) for i in range(9) for j in range(9) if arr[i][j] == 0]

# for i in range(N):
#     for j in range(N):
#         if arr[i][j] == 0:
#             zero_list.append((i,j))

dfs(0)
