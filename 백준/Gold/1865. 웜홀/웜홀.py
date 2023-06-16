import sys

input = sys.stdin.readline
INF = int(1e9)

def bf(start):
    dis = [INF] * (n+1)  # 최단거리 초기화
    dis[start]=0
    # 메인 로직
    # 음의 사이클 판별을 위해 n번 반복
    for i in range(n):
        for edge in edges:
            cur = edge[0]
            next_node = edge[1]
            cost = edge[2]
            
            if dis[next_node] > cost + dis[cur]:
                dis[next_node] = cost + dis[cur]
                # i==n-1이면 n번 돌렸을때도 갱신이 발생하면 음의 싸이클 존재
                if i == n - 1:
                    return True
    return False

t = int(input())

for _ in range(t):
    n, m, w = map(int, input().split())
    edges = []
    # 도로
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    # 웜홀
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    # 시작 위치는 무관
    key = bf(1)
    if key:
        print("YES")
    else:
        print("NO")