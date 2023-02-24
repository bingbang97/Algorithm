V = int(input())

graph = [[] for _ in range(V + 1)]

for _ in range(V):
  w = list(map(int, input().split()))
  for i in range(1, len(w) - 2, 2):
    graph[w[0]].append([w[i], w[i + 1]])

visited = [-1] * (V + 1)


def dfs(s, e):
  for a, b in graph[s]:
    if visited[a] == -1:
      visited[a] = b + e
      dfs(a, b + e)

visited[1] = 0
dfs(1, 0)

start = visited.index(max(visited))
visited = [-1] * (V + 1)
visited[start] = 0
dfs(start,0)

print(max(visited))

