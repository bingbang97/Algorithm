w, h = map(int, input().split())
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

d1, n1 = map(int, input().split())

sum_distance = 0

for i in range(N):
    d2 = arr[i][0]
    n2 = arr[i][1]
    temp = 0
    # if d1 == d2:
    #     temp = abs(n1 - n2)
    # elif d1 + d2 == 3:
    #     len1 = n1 + n2 + h
    #     len2 = h + w - n1 + w - n2
    #     if len1 > len2:
    #         temp = len2
    #     else:
    #         temp = len1
    # elif d1 + d2 == 7:
    #     len1 = n1 + n2 + w
    #     len2 = w + h - n1 + h - n2
    #     if len1 > len2:
    #         temp = len2
    #     else:
    #         temp = len1
    # else:
    #     if d1 == 1:
    #         if d2 == 3:
    #             temp = n1 + n2
    #         else:
    #             temp = w - n1 + n2
    #     elif d1 == 2:
    #         if d2 == 4:
    #             temp = w - n1 + h - n2
    #         else:
    #             temp = h - n2 + n1
    #     elif d1 == 3:
    #         if d2 == 1:
    #             temp = n1 + n2
    #         else:
    #             temp = h - n1 + n2
    #     else:
    #         if d2 == 2:
    #             temp = h - n1 + w - n2
    #         else:
    #             temp = h - n1 + n2
    if d1 == 1:
        if d2 == 1:
            temp = abs(n1 - n2)
        elif d2 == 2:
            len1 = n1 + n2 + h
            len2 = h + w - n1 + w - n2
            if len1 > len2:
                temp = len2
            else:
                temp = len1
        elif d2 == 3:
            temp = n1 + n2
        else:
            temp = w - n1 + n2
    elif d1 == 2:
        if d2 == 1:
            len1 = n1 + n2 + h
            len2 = h + w - n1 + w - n2
            if len1 > len2:
                temp = len2
            else:
                temp = len1
        elif d2 == 2:
            temp = abs(n1 - n2)
        elif d2 == 3:
            temp = n1 + h - n2
        else:
            temp = w - n1 + h - n2

    elif d1 == 3:
        if d2 == 1:
            temp = n1 + n2
        elif d2 == 2:
            temp = h - n1 + n2
        elif d2 == 3:
            temp = abs(n1 - n2)
        else:
            len1 = n1 + n2 + w
            len2 = w + h - n1 + h - n2
            if len1 > len2:
                temp = len2
            else:
                temp = len1
    else:
        if d2 == 1:
            temp = n1 + w - n2
        elif d2 == 2:
            temp = h - n1 + w - n2
        elif d2 == 3:
            len1 = n1 + n2 + w
            len2 = w + h - n1 + h - n2
            if len1 > len2:
                temp = len2
            else:
                temp = len1
        else:
            temp = abs(n1 - n2)
    sum_distance += temp

print(sum_distance)
