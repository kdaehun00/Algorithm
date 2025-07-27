"""
N - 정점의 개수
M - 간선의 개수
u, v - 간선의 양 끝점
"""
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
edge = [[] for _ in range(N+1)]
chk = [False for _ in range(N+1)]

for _ in range(M):
  u, v = map(int, input().split())
  edge[u].append(v)
  edge[v].append(u)

for e in edge:
  e.sort()

def bfs(data):
  q = deque()
  q.append(data)
  chk[data] = True
  while q:
    node = q.popleft()
    for nxt in (edge[node]):
      if not chk[nxt]:
        chk[nxt] = True
        q.append(nxt)

count = 0
for i in range(1, N+1):
  if not chk[i]:
    count += 1
    bfs(i)

print(count)