def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
true_arr = list(map(int, input().split()))[1:]

parent = list(range(N + 1))

for i in true_arr:
    parent[i] = 0

party_arr = []

for _ in range(M):
    n, *tmp_arr = map(int, input().split())
    party_arr.append(tmp_arr)
    if not tmp_arr:
        continue

    for i in range(n - 1):
        union(tmp_arr[i], tmp_arr[i + 1])

ans = 0

for party in party_arr:
    for i in party:
        if not find(parent[i]):
            break
    else:
        ans += 1

print(ans)
