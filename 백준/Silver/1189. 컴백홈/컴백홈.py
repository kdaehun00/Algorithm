"""
R, C - 세로, 가로
K - target 거리
"""
import sys
from collections import deque

input = sys.stdin.readline

R, C, K = map(int, input().split())
road = [list(map(str, input().strip())) for _ in range(R)]

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

result = 0


def dfs(y, x, dist, chk):
  global result

  if y == 0 and x == C - 1:
    if dist == K:
      result += 1
    return

  for i in range(4):
    ny = y + dy[i]
    nx = x + dx[i]
    if 0 <= ny < R and 0 <= nx < C:
      if not chk[ny][nx] and road[ny][nx] == '.':
        chk[ny][nx] = True
        dfs(ny, nx, dist + 1, chk)
        chk[ny][nx] = False

chk = [[False] * C for _ in range(R)]
chk[R - 1][0] = True
dfs(R - 1, 0, 1, chk)
print(result)
