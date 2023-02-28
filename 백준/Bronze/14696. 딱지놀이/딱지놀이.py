N = int(input())
for tc in range(N):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    arr_A = [0] * 4
    arr_B = [0] * 4

    for i in range(1, len(A)):
        arr_A[A[i] - 1] += 1
    for i in range(1, len(B)):
        arr_B[B[i] - 1] += 1

    ans = 'D'

    for i in range(3, -1, -1):
        if arr_A[i] > arr_B[i]:
            ans = 'A'
            break
        elif arr_A[i] < arr_B[i]:
            ans = 'B'
            break

    print(ans)
