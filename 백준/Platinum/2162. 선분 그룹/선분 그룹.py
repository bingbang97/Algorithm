N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
parent = [-1 for _ in range(N)]


def ccw(a1, b1, a2, b2, a3, b3):
    tmp = (a2 - a1) * (b3 - b1) - (a3 - a1) * (b2 - b1)
    if tmp > 0:
        return 1
    elif tmp == 0:
        return 0
    else:
        return -1


def check(x1, y1, x2, y2, x3, y3, x4, y4):
    tmp1 = ccw(x1, y1, x2, y2, x3, y3)
    tmp2 = ccw(x1, y1, x2, y2, x4, y4)
    tmp3 = ccw(x3, y3, x4, y4, x1, y1)
    tmp4 = ccw(x3, y3, x4, y4, x2, y2)
    # 같은 직선 상에 있는 경우, 선분이 겹치는지 판단
    if tmp1 * tmp2 == 0 and tmp3 * tmp4 == 0:
        if min(x1, x2) <= max(x3, x4) and max(x1, x2) >= min(x3, x4) \
                and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
            return True
    # 서로 교차할 경우 음수나 0이 나옴
    elif tmp1 * tmp2 <= 0 and tmp3 * tmp4 <= 0:
        return True
    return False


def find(x):
    if parent[x] < 0:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if parent[x] < parent[y]:
        parent[x] += parent[y]
        parent[y] = x
    else:
        parent[y] += parent[x]
        parent[x] = y


for i in range(N - 1):
    for j in range(i + 1, N):
        if check(*arr[i], *arr[j]):
            union(i, j)


cnt = 0
ans = 0
for i in range(N):
    if parent[i] < 0:
        cnt += 1
        ans = max(ans, abs(parent[i]))

print(cnt)
print(ans)
