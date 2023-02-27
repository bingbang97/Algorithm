n = int(input())
m = int(input())
INF = int(1e9)
arr = [[INF]*n for _ in range(n)]

for i in range(m):
    s, e, cost = map(int, input().split())
    if arr[s-1][e-1] > cost:
        arr[s-1][e-1] = cost

for i in range(n):
    arr[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

for i in range(n):
    for j in range(n):
        if arr[i][j] == INF:
            arr[i][j] = 0
            
for i in range(n):
    print(*arr[i])


