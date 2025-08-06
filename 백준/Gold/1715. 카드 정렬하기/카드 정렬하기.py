import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    heapq.heappush(heap, int(input()))

total = 0

while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    cost = a + b
    total += cost
    heapq.heappush(heap, cost)

print(total)