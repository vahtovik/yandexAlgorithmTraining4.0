n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
max_len = 0

for i in range(n):
    dp[i][0] = data[i][0]
    max_len = max(max_len, dp[i][0])

for j in range(m):
    dp[0][j] = data[0][j]
    max_len = max(max_len, dp[0][j])

for i in range(1, n):
    for j in range(1, m):
        if data[i][j] == 1:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
            max_len = max(max_len, dp[i][j])

print(max_len)
