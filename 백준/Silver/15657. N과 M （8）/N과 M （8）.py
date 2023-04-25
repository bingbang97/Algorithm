N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = []

def dfs(depth, idx, n, m):
    if depth == m:
        print(' '.join(map(str, ans)))
        return
    for i in range(idx, n):
        ans.append(arr[i])
        dfs(depth+1, i, n, m)
        ans.pop()

dfs(0, 0, N, M)