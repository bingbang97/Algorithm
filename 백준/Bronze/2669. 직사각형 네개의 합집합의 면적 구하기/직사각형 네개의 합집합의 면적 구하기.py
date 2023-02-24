N = 100
arr = [[0]*N for _ in range(N)]

for _ in range(4):
    x, y, l, h = map(int, input().split())
    for i in range(x, l):
        for j in range(y, h):
            arr[i][j] = 1

cnt = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            cnt += 1

print(cnt)