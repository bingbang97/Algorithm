N = int(input())

num_list = list(map(int, input().split()))
student_list = []

for i in range(N):
    student_list.insert(num_list[i], i+1)

student_list.reverse()

print(*student_list)
