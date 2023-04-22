def h(n, r, k, s):
    if k == r:
        print(*temp)
    else:
        for i in range(s, n):
            temp[k] = arr[i]
            h(n, r, k + 1, i)


N, M = map(int, input().split())

arr = list(range(1, N + 1))
temp = [0] * M
h(N, M, 0, 0)
