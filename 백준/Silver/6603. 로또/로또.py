def comb(n, r, k, s):
    if k == r:
        print(*t)
    else:
        for i in range(s, n - r + 1 + k):
            t[k] = a[i]
            comb(n, r, k + 1, i + 1)


arr = []
while True:
    tmp = list(map(int, input().split()))
    tmp.pop(0)
    if tmp:
        arr.append(tmp)
    else:
        break
T = len(arr)
for tc in range(T):
    a = arr[tc]
    N = len(a)
    R = 6
    t = [0] * R
    comb(N, R, 0, 0)
    print()
