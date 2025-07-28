import sys

input = sys.stdin.readline

n = int(input())

cost = list(map(int, input().split()))

current_sum = cost[0]
max_sum = cost[0]

for i in range(1, n):
  current_sum = max(cost[i], current_sum + cost[i])
  max_sum = max(max_sum, current_sum)

print(max_sum)