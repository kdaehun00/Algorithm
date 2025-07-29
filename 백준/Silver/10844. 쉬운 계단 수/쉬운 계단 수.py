import sys

input = sys.stdin.readline

MOD = 10**9
N = int(input())

dp = [[0]*10 for _ in range(N+1)]

for i in range(1, 10):
    dp[1][i] = 1

for n in range(2, N+1):
    for k in range(10):
        if k > 0:
            dp[n][k] += dp[n-1][k-1]
        if k < 9:
            dp[n][k] += dp[n-1][k+1]
        dp[n][k] %= MOD

print(sum(dp[N]) % MOD)