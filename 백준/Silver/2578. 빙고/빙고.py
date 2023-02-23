bingo_board = [list(map(int, input().split())) for _ in range(5)]

ans_list = []

for i in range(5):
    list1 = list(map(int, input().split()))
    for j in range(5):
        ans_list.append(list1[j])

for k in range(25):

    for i in range(5):
        for j in range(5):
            if ans_list[k] == bingo_board[i][j]:
                bingo_board[i][j] = 0

    cnt = 0
    for i in range(5):
        flag = 1
        for j in range(5):
            if bingo_board[i][j] != 0:
                flag = 0
                break
        if flag:
            cnt += 1

    for j in range(5):
        flag = 1
        for i in range(5):
            if bingo_board[i][j] != 0:
                flag = 0
                break
        if flag:
            cnt += 1
    flag = 1
    for i in range(5):
        if bingo_board[i][i] != 0:
            flag = 0
            break
    if flag:
        cnt += 1
    flag = 1
    for i in range(5):
        if bingo_board[i][4-i] != 0:
            flag = 0
            break
    if flag:
        cnt += 1

    if cnt >= 3:
        break
print(k+1)
