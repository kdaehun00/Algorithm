"""
N - 보석의 개수
M, V - 각 보석의 무게와 가격
K - 가방의 개수
"""
import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())
jewels = [list(map(int, input().split())) for _ in range(N)]
bags = [int(input().strip()) for _ in range(K)]

jewels.sort()
bags.sort()

result = 0
heap = []
idx = 0

for bag in bags:
  while idx < N and jewels[idx][0] <= bag:
    heapq.heappush(heap, -jewels[idx][1])
    idx += 1

  if heap:
    result += -heapq.heappop(heap)

print(result)