n = int(input())
data = list(map(int, input().split()))
left_sums, right_sums, length, total = [], [], len(data), 0

for num in data:
    total += num
    left_sums.append(total)

total = 0
for num in reversed(data):
    total += num
    right_sums.append(total)

right_sums = list(reversed(right_sums))
right_sums.append(0)

for i, num in enumerate(data, start=1):
    left_total = num * i - left_sums[i - 1]
    right_total = right_sums[i] - (length - i) * num
    print(left_total + right_total, end=' ')
