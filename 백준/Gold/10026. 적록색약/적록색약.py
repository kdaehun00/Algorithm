"""
V - 정점의 갯수
E - 간선의 갯수
K - 시작 정점
u, v, w - u -> v 사이의 w 가중치
"""

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
draw = [list(map(str, input().strip())) for _ in range(N)]
non_draw = [['R' if c == 'G' else c for c in row] for row in draw]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def bfs(y, x, text, board, chk):
  q = deque()
  q.append((y, x))
  chk[y][x] = True

  while q:
    y, x = q.popleft()
    for dir in range(4):
      ey = y + dy[dir]
      ex = x + dx[dir]
      if 0 <= ey < N and 0 <= ex < N:
        if not chk[ey][ex] and board[ey][ex] == text:
          chk[ey][ex] = True
          q.append((ey, ex))


chk_normal = [[False] * N for _ in range(N)]
count_normal = 0
for y in range(N):
  for x in range(N):
    if not chk_normal[y][x]:
      text = draw[y][x]
      count_normal += 1
      bfs(y, x, text, draw, chk_normal)

chk_cb = [[False] * N for _ in range(N)]
count_cb = 0
for y in range(N):
  for x in range(N):
    if not chk_cb[y][x]:
      text = non_draw[y][x]
      count_cb += 1
      bfs(y, x, text, non_draw, chk_cb)

print(count_normal, count_cb)