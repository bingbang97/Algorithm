N, M = map(int,input().split())
arr = sorted(list(map(int,input().split())))
ans = []

def dfs(idx, cnt):
    if cnt==M:
        print(*ans)
        return
    
    for i in range(idx, N):
        idx+=1
        ans.append(arr[i])
        dfs(idx, cnt+1)
        ans.pop()
        
dfs(0,0)