N = int(input())
arr = list(map(int, input().split()))

st = int(input())
st_arr = [list(map(int, input().split())) for _ in range(st)]

for i in range(st):
    if st_arr[i][0] == 1:
        j = st_arr[i][1]
        k = 1
        while True:
            idx = j * k
            if idx > N:
                break
            arr[idx - 1] = (arr[idx - 1] + 1) % 2
            k += 1
    if st_arr[i][0] == 2:
        j = st_arr[i][1] - 1
        flag = 1
        k = 1
        while flag:
            if j + k > N-1 or j - k < 0:
                flag = 0
            elif arr[j - k] == arr[j + k]:
                arr[j - k] = (arr[j - k] + 1) % 2
                arr[j + k] = (arr[j + k] + 1) % 2
                k += 1
            else:
                flag = 0

        arr[j] = (arr[j] + 1) % 2
for i in range(0, N, 20):
    print(*arr[i:i + 20])

