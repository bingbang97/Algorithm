import heapq

V, E = map(int, input().split())
V += 1
INF = int(1e9)
s = int(input())
graph = [[] * V for _ in range(V)]
distance = [INF] * V

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# 다잌스트라 함수
def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            current_cost = distance[now] + i[1]

            if current_cost < distance[i[0]]:
                distance[i[0]] = current_cost
                heapq.heappush(q, (current_cost, i[0]))


dijkstra(s)

for i in range(1, V):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

