import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())

edge = [[] for _ in range(N + 1)]

for i in range(M):
  v1, v2 = map(int, input().split())
  edge[v1].append(v2)
  edge[v2].append(v1)

for e in (edge):
  e.sort()

def dfs(start, visited, result):
  visited[start] = True
  result.append(start)
  for nxt in edge[start]:
    if not visited[nxt]:
      dfs(nxt, visited, result)

def bfs(start, visited):
  result = []
  q = deque([start])
  visited[start] = True

  while q:
    cur = q.popleft()
    result.append(cur)
    for nxt in edge[cur]:
      if not visited[nxt]:
        visited[nxt] = True
        q.append(nxt)
  return result

visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)
dfs_result = []
dfs(V, visited_dfs, dfs_result)
bfs_result = bfs(V, visited_bfs)

print(' '.join(map(str, dfs_result)))
print(' '.join(map(str, bfs_result)))