def comb(n, r, k, s):
    if k == r:
        print(*temp)
    else:
        for i in range(s, n):
            temp[k] = arr[i]
            comb(n, r, k + 1, i + 1)


N, M = map(int, input().split())

arr = list(range(1, N + 1))
temp = [0] * M
comb(N, M, 0, 0)
