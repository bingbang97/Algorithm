T = int(input())

def recur(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    else:
        return recur(n-1) + recur(n-2) + recur(n-3)
    
for tc in range(T):
    print(recur(int(input())))