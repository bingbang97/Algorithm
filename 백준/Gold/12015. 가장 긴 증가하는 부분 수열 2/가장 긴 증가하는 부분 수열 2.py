n = int(input())
arr = list(map(int, input().split()))
tmp = [0]

for num in arr:
    if tmp[-1] < num:
        tmp.append(num)
    else:
        l = 0
        r = len(tmp)
        while l < r:
            mid = (r + l) // 2
            if tmp[mid] < num:
                l = mid + 1
            else:
                r = mid
        tmp[r] = num

print(len(tmp) - 1)