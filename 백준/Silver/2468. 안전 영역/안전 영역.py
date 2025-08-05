import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

def dfs(map_arr, chk, y, x):
  q = deque()
  q.append((y, x))
  while q:
    y, x = q.pop()
    chk[y][x] = True
    for i in range(4):
      ey = y + dy[i]
      ex = x + dx[i]
      if 0 <= ey < N and 0 <= ex < N:
        if not chk[ey][ex] and map_arr[ey][ex] > 0:
          chk[ey][ex] = True
          q.append((ey, ex))

def bfs(map_arr):
  chk = [[False] * N for _ in range(N)]
  count = 0
  for y in range(N):
    for x in range(N):
      if not chk[y][x] and map_arr[y][x] > 0:
        dfs(map_arr, chk, y, x)
        count += 1
  return count

max_count = 0
for i in range(101):
  real_map = [[0] * N for _ in range(N)]
  for y in range(N):
    for x in range(N):
      real_map[y][x] = arr[y][x] - i
  max_count = max(max_count, bfs(real_map))

print(max_count)