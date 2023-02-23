N, R = map(int, input().split())

n = 1
for i in range(R):
    n *= N
    N -= 1
r = 1
for i in range(2, R + 1):
    r *= i

print((n // r))

