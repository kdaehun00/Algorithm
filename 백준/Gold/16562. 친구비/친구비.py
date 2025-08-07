"""
N - 학생 수 ( 1 <= N <= 10,000 )
M - 친구 관계 수 ( 0 <= M <= 10,000 )
A - 돈을 준 금액 ( 1 <= A <= 10,000 )
k - 가지고 있는 돈 ( 1 <= k <= 10,000,000 )

10^4 이므로
O(M*N) 까지 가능!
"""
import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N, M, k = map(int, input().split())
friend_money = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N+1)]

for _ in range(M):
  v, w = map(int, input().split())
  graph[v].append(w)
  graph[w].append(v)

visited = [False] * (N + 1)

def dfs(v, group):
  visited[v] = True
  group.append(v)
  for nxt in graph[v]:
    if not visited[nxt]:
      dfs(nxt, group)

total_cost = 0

for i in range(1, N+1):
  if not visited[i]:
    group = []
    dfs(i, group)
    min_cost = min(friend_money[j] for j in group)
    total_cost += min_cost

if total_cost <= k:
  print(total_cost)
else:
  print("Oh no")
