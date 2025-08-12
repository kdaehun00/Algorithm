import sys
from collections import deque
input = sys.stdin.readline

# 상, 하, 좌, 우, 우상, 좌상, 우하, 좌하
dy = [-1, 1, 0, 0, -1, -1, 1, 1]
dx = [0, 0, -1, 1, 1, -1, 1, -1]

def dfs(land, chk, y, x):
  q = deque()
  q.append((y, x))
  while q:
    y, x = q.popleft()
    for i in range(8):
      ny = y + dy[i]
      nx = x + dx[i]
      if 0 <= ny < h and 0 <= nx < w:
        if land[ny][nx] == 1 and not chk[ny][nx]:
          q.append((ny, nx))
          chk[ny][nx] = True

def bfs(land, chk):
  count = 0
  for y in range(h):
    for x in range(w):
      if 0 <= y < h and 0 <= x < w:
        if land[y][x] == 1 and not chk[y][x]:
          chk[y][x] = True
          count += 1
          dfs(land, chk, y, x)
  return count

while True:
  w, h = map(int, input().split())
  if w == 0 and h == 0:
    break

  land = [list(map(int, input().split())) for _ in range(h)]
  chk = [[False] * w for _ in range(h)]
  print(bfs(land, chk))
