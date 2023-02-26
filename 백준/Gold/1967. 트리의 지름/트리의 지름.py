import sys
sys.setrecursionlimit(10**5)
n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
  w = list(map(int, input().split()))
  graph[w[0]].append([w[1], w[2]])
  graph[w[1]].append([w[0], w[2]])

visited = [-1] * (n+1)

def dfs(s, e):
  for a, d in graph[s]:
    if visited[a] == -1:
      visited[a] = d + e
      dfs(a, d + e)

visited[1] = 0
dfs(1, 0)

start = visited.index(max(visited))
visited = [-1] * (n + 1)
visited[start] = 0
dfs(start,0)

print(max(visited))