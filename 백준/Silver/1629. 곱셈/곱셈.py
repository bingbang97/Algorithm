def DaC(a,b,c):
    if b == 1:
        return a % c
    tmp = DaC(a, b//2, c)
    
    if not (b % 2):
        return(tmp * tmp % c)
    
    else:
        return tmp * tmp * a % c
    
A, B, C = map(int, input().split())

print(DaC(A, B, C))
    