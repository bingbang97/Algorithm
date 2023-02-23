N = int(input())
A = list(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))
A.sort()

# arr의 각 원소별로 이분탐색
for num in arr:
    l, r = 0, N - 1
    ans = 0
    while l <= r:
        mid = (l + r) // 2
        if num == A[mid]:
            ans = 1
            print(1)
            break
        elif num > A[mid]:
            l = mid + 1
        else:
            r = mid - 1

    if not ans:
        print(0)
