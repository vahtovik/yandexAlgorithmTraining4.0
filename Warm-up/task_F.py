k = int(input())
n = int(input())
data = [int(input()) for _ in range(n)]
current, time, weight = len(data) - 1, 0, 0

while current >= 0:
    if data[current] // k > 0:
        time += data[current] // k * (current + 1) * 2
        data[current] %= k
        while data[current] == 0 and current >= 0:
            current -= 1
    elif data[current] > 0:
        weight += data[current]
        time += (current + 1) * 2
        data[current] = 0
        while data[current] == 0 and current >= 0:
            current -= 1
        while weight < k and current >= 0:
            if data[current] > k - weight:
                data[current] -= k - weight
                weight += k - weight
            else:
                weight += data[current]
                data[current] = 0
                current -= 1
    else:
        current -= 1
    weight = 0

print(time)
