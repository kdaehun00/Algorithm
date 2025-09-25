import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
chk = [[0]*(n+1) for _ in range(n+1)]

for _ in range(k):
    a, b = map(int, input().split())
    graph[a].append(b)

def dfs(start, node):
    for nxt in graph[node]:
        if not chk[start][nxt]:
            chk[start][nxt] = 1
            dfs(start, nxt)

for i in range(1, n+1):
    dfs(i, i)

s = int(input())
for _ in range(s):
    a, b = map(int, input().split())
    if chk[a][b]:
        print(-1)
    elif chk[b][a]:
        print(1)
    else:
        print(0)