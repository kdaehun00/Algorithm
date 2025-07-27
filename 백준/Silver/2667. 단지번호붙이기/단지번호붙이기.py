import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
apart = [list(map(int, input().strip())) for _ in range(N)]
chk = [[False] * N for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(y, x):
  q = deque()
  q.append((y, x))
  chk[y][x] = True
  count = 1

  while q:
    cy, cx = q.popleft()
    for dir in range(4):
      ny = cy + dy[dir]
      nx = cx + dx[dir]

      if 0 <= ny < N and 0 <= nx < N:
        if apart[ny][nx] == 1 and chk[ny][nx] == False:
          chk[ny][nx] = True
          q.append((ny, nx))
          count += 1
  return count

house_counts = []
complex_count = 0

for y in range(N):
  for x in range(N):
    if apart[y][x] == 1 and chk[y][x] == False:
      house_size = bfs(y, x)
      house_counts.append(house_size)
      complex_count += 1

print(complex_count)
for count in sorted(house_counts):
  print(count)