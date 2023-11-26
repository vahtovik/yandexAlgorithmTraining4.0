a = int(input())
b = int(input())
n = int(input())

print('Yes' if a > b // n + bool(b % n) else 'No')
