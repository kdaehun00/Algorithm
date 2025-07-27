"""
V - 정점의 갯수
E - 간선의 갯수
K - 시작 정점
u, v, w - u -> v 사이의 w 가중치
"""

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
K = int(input())

edge = [[] for _ in range(V + 1)]
distance = [INF] * (V+1)

for _ in range(E):
  u, v, w = map(int, input().split())
  edge[u].append((v, w))

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue

    for next_node, weight in edge[now]:
      cost = dist + weight
      if cost < distance[next_node]:
        distance[next_node] = cost
        heapq.heappush(q, (cost, next_node))

dijkstra(K)

for i in range(1, V + 1):
  print("INF" if distance[i] == INF else distance[i])