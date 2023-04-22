def solve(num, op):
    while len(op):
        tmp_op = op.pop(0)
        a, b = num.pop(0), num.pop(0)
        if tmp_op == '+':
            tmp_num = a + b
            num.insert(0, tmp_num)
        elif tmp_op == '*':
            tmp_num = a * b
            num.insert(0, tmp_num)
        elif tmp_op == '-':
            tmp_num = a - b
            num.insert(0, tmp_num)
    return num[0]
# 마지막 계산


def calculate(top, num, op):
    global ans
    if len(num) == 1 or top == N // 2:
        ans = max(ans, solve(num, op))
        return
    # 최댓값인지 아닌지 비교하는 방법

    calculate(top + 1, num[:], op[:])
    try:
        a, b = num.pop(top), num.pop(top)
        tmp_op = op.pop(top)
        if tmp_op == '+':
            tmp_num = a + b
            num.insert(top, tmp_num)
        elif tmp_op == '*':
            tmp_num = a * b
            num.insert(top, tmp_num)
        elif tmp_op == '-':
            tmp_num = a - b
            num.insert(top, tmp_num)

        calculate(top + 1, num[:], op[:])

    except:
        pass


N = int(input())
temp = input()

num_stack = []
op_stack = []
ans = -2 ** 31 - 1
for i in range(N):
    if temp[i].isnumeric():
        num_stack.append(int(temp[i]))
    else:
        op_stack.append(temp[i])

calculate(0, num_stack, op_stack)
print(ans)
