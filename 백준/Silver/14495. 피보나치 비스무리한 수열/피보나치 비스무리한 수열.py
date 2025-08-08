import sys

input = sys.stdin.readline

N = int(input())
dp = [0] * (N+1)

if N >= 1: dp[1] = 1
if N >= 2: dp[2] = 1
if N >= 3: dp[3] = 1

for n in range(4, N+1):
  dp[n] = dp[n-1] + dp[n-3]

print(dp[N])