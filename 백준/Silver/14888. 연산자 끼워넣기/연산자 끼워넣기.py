def dfs(idx, tmp):
    global a, s, m, d, min_val, max_val
    if idx == N:
        max_val = max(max_val, tmp)
        min_val = min(min_val, tmp)
    else:
        idx += 1
        # idx 하나 증가시키고 실행
        if a > 0:
            a -= 1
            dfs(idx, tmp + arr[idx-1])
            a += 1
        if s > 0:
            s -= 1
            dfs(idx, tmp - arr[idx-1])
            s += 1
        if m > 0:
            m -= 1
            dfs(idx, tmp * arr[idx-1])
            m += 1
        if d > 0:
            d -= 1
            dfs(idx, int(tmp / arr[idx-1]))
            # C++14의 나누기 기준을 따르기 위하여 방식을 취했음.
            # (인터넷 찾아봄..그냥 몫으로 하니깐 틀리게 나옴...)
            d += 1


N = int(input())
arr = list(map(int, input().split()))
a, s, m, d = map(int, input().split())
min_val = 1e9
max_val = -1 * 1e9
# 지수 표현 방법 1e9 => 1 * (10**9)

dfs(1, arr[0])
# 왼쪽에서부터 들어가야하기에 arr[0]부터 시작

print(max_val)
print(min_val)
