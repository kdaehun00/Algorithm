import sys
from collections import deque

input = sys.stdin.readline

V = int(input())
E = int(input())

edge = [[] for _ in range(V + 1)]
for i in range(E):
  v1, v2 = map(int, input().split())
  edge[v1].append(v2)
  edge[v2].append(v1)

for e in edge:
  e.sort()

chk = [False] * (V + 1)
result = 0

q = deque()
q.append(1)

while q:
  com = q.pop()
  if not chk[com]:
    chk[com] = True
    result += 1
    for i in edge[com]:
      q.append(i)

print(result - 1)
