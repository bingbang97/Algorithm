num = int(1e6)


eratosthenes = [True for _ in range(num)]

#에라토스테네스의 체
for i in range(2,int(num**0.6)):
    if eratosthenes[i]==True:
        for j in range(i*2, num, i) : 
            if eratosthenes[j] == True :
                eratosthenes[j] = False
                
import sys
input = sys.stdin.readline

while(True):
    n = int(input())
    if n==0 : break
    for i in range(3,num):
        if eratosthenes[i] == True:
            if eratosthenes[n-i] == True :
                print("%d = %d + %d"%(n , i , n-i))
                break