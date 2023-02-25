N = int(input())
arr = list(map(int, input().split()))
NGE = [-1]*N
stack = []

for i in range(N):
    while stack and arr[stack[-1]] < arr[i]:
        NGE[stack.pop()] = arr[i]
    stack.append(i)
print(*NGE)
