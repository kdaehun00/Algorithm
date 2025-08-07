"""
N - 반복 횟수
A, B - 연결된 방의 정보
C - 길의 길이 ( 1 <= C <= 1,000,000,000 )

메모리 1024MB -> 2^10
O(n) 정도만 가능
"""
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input())

room_dist = [[] for _ in range(N+1)]
for _ in range(N-1):
  a, b, c = map(int, input().split())
  room_dist[a].append((b, c))
  room_dist[b].append((a, c))

chk = [False] * (N+1)
max_dist = 0
def dfs(node, dist):
  global max_dist
  chk[node] = True
  max_dist = max(max_dist, dist)

  for next_node, cost in room_dist[node]:
    if not chk[next_node]:
      dfs(next_node, dist + cost)

dfs(1, 0)
print(max_dist)