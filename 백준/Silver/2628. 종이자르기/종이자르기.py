y , x = map(int, input().split())

N = int(input())

cutting_list = [list(map(int, input().split())) for _ in range(N)]

x_list = []
y_list = []

for i in range(N):
    if cutting_list[i][0] == 0:
        x_list.append(cutting_list[i][1])
    else:
        y_list.append(cutting_list[i][1])

x_list.sort()
y_list.sort()
x_cutting_list = []
y_cutting_list = []

for i in range(len(x_list)):
    x_cutting_list.append(x - x_list[-1-i])
    x -= x - x_list[-1-i]
x_cutting_list.append(x)

for i in range(len(y_list)):
    y_cutting_list.append(y - y_list[-1-i])
    y -= y - y_list[-1-i]
y_cutting_list.append(y)

max_area = 0
for i in x_cutting_list:
    for j in y_cutting_list:
        if i*j > max_area:
            max_area = i*j

print(max_area)

