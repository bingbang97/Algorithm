for _ in range(int(input())):
    N, M, x, y = map(int, input().split())
    ans = x
    while True:
        if (ans - x) % N == 0 and (ans - y) % M == 0:
            break
        ans += N
        if ans > N*M:
            ans = -1
            break
    print(ans)
