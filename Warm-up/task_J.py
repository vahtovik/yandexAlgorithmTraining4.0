from math import floor

t = int(input())

for _ in range(t):
    n, a, b = map(int, input().split())
    if floor(n / b) != floor(n / a) or (a == b and n % a == 0):
        print('YES')
    else:
        print('NO')
