N = int(input())
INF = 10001

dp = [INF] * (N + 1)
dp[0] = 0

for i in range(3, N + 1):
    if i >= 3:
        dp[i] = min(dp[i], dp[i - 3] + 1)
    if i >= 5:
        dp[i] = min(dp[i], dp[i - 5] + 1)

print(dp[N] if dp[N] != INF else -1)