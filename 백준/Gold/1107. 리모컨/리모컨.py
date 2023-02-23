number = int(input())
n = int(input())
if n:
    error_num = list(input().split())
else:
    error_num = []


ans = abs(number-100)

for num in range(1000001):
    for i in str(num):
        if i in error_num:
            break
    else:
        ans = min(ans, len(str(num)) + abs(number-num))

print(ans)