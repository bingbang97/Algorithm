N, K = map(int, input().split())
student_list = []
for i in range(N):
    student_info = tuple(map(int, input().split()))
    student_list.append(student_info)

student_dict = dict()
for i in range(N):
    if student_list[i] not in student_dict:
        student_dict[student_list[i]] = 1
    else:
        student_dict[student_list[i]] += 1
st_num_list = list(student_dict.values())

cnt = 0

for i in range(len(st_num_list)):
    cnt += (st_num_list[i]+1) // 2

print(cnt)