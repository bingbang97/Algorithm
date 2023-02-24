def prim(r, N):
    MST = [0]* N
    key = [1e6] *N
    key[r] = 0
    for _ in range(N):
        u = 0
        min_value = 1e6
        for i in range(N):
            if MST[i] == 0 and key[i] < min_value:
                u = i
                min_value = key[i]

        MST[u] = 1

        for n in range(N):
            if MST[n] == 0 and distance[u][n] > 0:
                key[n] = min(key[n], distance[u][n])

    return key


T = int(input())
for tc in range(T):
    N = int(input())
    dx = list(map(int, input().split()))
    dy = list(map(int, input().split()))
    E = float(input())

    distance = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            distance[i][j] = ((dx[i] -dx[j])**2 + (dy[i]-dy[j])**2)**(1/2)

    distance_list = prim(0,N)
    ans = 0
    for i in range(len(distance_list)):
        ans += ((distance_list[i])**2) * E
    print(f'#{tc+1} {round(ans)}')
