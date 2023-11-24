n, m = map(int, input().split())
data = [0] + list(map(int, input().split()))
data_r = [0] + list(reversed(data[1:]))

p = 10 ** 9 + 7
x_ = 257
h, hr = [0] * (n + 1), [0] * (n + 1),
x = [0] * (n + 1)
x[0] = 1

for i in range(1, n + 1):
    h[i] = (h[i - 1] * x_ + data[i]) % p
    hr[i] = (hr[i - 1] * x_ + data_r[i]) % p
    x[i] = (x[i - 1] * x_) % p

res = []
for k in range(n // 2 + 1):
    h1 = h[k]
    h2 = (hr[n - k] - hr[n - 2 * k] * x[k]) % p
    if h1 == h2:
        res.append(n - k)

print(*reversed(res))
