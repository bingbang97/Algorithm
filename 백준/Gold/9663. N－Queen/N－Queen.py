def n_queen(k):
    global cnt
    if k == N:
        cnt += 1
        return
    else:
        for j in range(N):
            flag = True
            for i in range(k):
                if abs(i - k) == abs(arr[i] - j) or arr[i] == j:
                    flag = False
                    break
            if flag:
                arr[k] = j
                n_queen(k + 1)
    return

N = int(input())
arr = [0] * N
cnt = 0
n_queen(0)
print(cnt)