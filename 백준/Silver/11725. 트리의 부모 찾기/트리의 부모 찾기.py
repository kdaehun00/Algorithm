import sys

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]
parent_node = [0] * (N + 1)

for _ in range(N - 1):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

def dfs(start):
  q = [start]
  while q:
    now = q.pop()
    for nxt in graph[now]:
      if parent_node[nxt] == 0:
        parent_node[nxt] = now
        q.append(nxt)

for node in range(1, N+1):
  if parent_node[node] == 0:
    dfs(node)

for result in range(2, N+1):
  print(parent_node[result])