N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

def dfs(dept):
    if dept == M:
        print(*path)
        return
    for i in range(N):
        path.append(arr[i])
        dfs(dept+1)
        path.pop()

path = []
dfs(0)