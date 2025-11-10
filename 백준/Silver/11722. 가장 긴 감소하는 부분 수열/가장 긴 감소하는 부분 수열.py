import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [1]*N
now_max_data = A[0]

for i in range(N):
  for j in range(i):
    if A[j] > A[i]:
      dp[i] = max(dp[i], dp[j]+1)

print(max(dp))