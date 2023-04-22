from collections import deque

N, K = map(int, input().split())

visited = [0 for _ in range(100001)] 

visited[N] = 1

queue = deque()
queue.append(N)

while queue:
  x = queue.popleft()
  if x == K:
    print(visited[x] -1)
    break
  
  if 0 <= x-1 <= 100000 and visited[x-1] == 0:
    visited[x-1] = visited[x] + 1
    queue.append(x-1)

  if 0 < 2*x <= 100000 and visited[2*x] == 0:
    visited[2*x] = visited[x]
    queue.appendleft(2*x)

  if 0 <= x+1 <= 100000 and visited[x+1] == 0:
    visited[x+1] = visited[x] + 1
    queue.append(x+1)
