N = int(input())
arr = list(map(int, input().split()))
max_length = 1
temp1 = 1
temp2 = 1
for i in range(N-1):
    if arr[i] <= arr[i + 1]:
        temp1 += 1
        if max_length < temp1:
            max_length = temp1
        else:
            max_length
    else:
        temp1 = 1

for i in range(N-1):
    if arr[i] >= arr[i + 1]:
        temp2 += 1
        if max_length < temp2:
            max_length = temp2
        else:
            max_length
    else:
        temp2 = 1

print(max_length)
