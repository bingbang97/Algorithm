def comb1(n, r, k, s):
    if k == r:
        foods.append(t[:])
    else:
        for i in range(s, n - r + 1 + k):
            t[k] = ingredient[i]
            comb1(n, r, k + 1, i + 1)


def comb2(n, r, k, s):
    if k == r:
        tmp.append(tmp1[:])
    else:
        for i in range(s, n - r + 1 + k):
            tmp1[k] = food[i]
            comb2(n, r, k + 1, i + 1)


N = int(input())
taste_list = [list(map(int, input().split())) for _ in range(N)]
ingredient = list(range(N))
R = N//2
t = [0] * R
foods = []
comb1(N, R, 0, 0)
ans = []
for food in foods:
    tmp = []
    tmp1 = [0] * 2
    comb2(N//2, 2, 0, 0)
    taste = 0
    for i in range(len(tmp)):
        taste += taste_list[tmp[i][0]][tmp[i][1]]
        taste += taste_list[tmp[i][1]][tmp[i][0]]
    ans.append(taste)

min_ans = abs(ans[0]-ans[-1])

for i in range(len(ans)//2):
    min_ans = min(min_ans, abs(ans[i]-ans[-i-1]))


print(min_ans)