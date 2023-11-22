n = int(input())
data = list(map(int, input().split()))
x = int(input())
less_x = 0
greater_x = 0

for num in data:
    if num < x:
        less_x += 1
    else:
        greater_x += 1

print(less_x)
print(greater_x)
