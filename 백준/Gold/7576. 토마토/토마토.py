"""
M - 상자의 가로 칸의 수
N - 상자의 세로 칸의 수

아이디어:
1. 1인 지점 찾기
2. 상하좌우가 0인 값을 queue에 넣기
3. 모두 다 처리 후 +1일 하고 다시 q의 값을 모두 처리
"""

import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())
tomato_map = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

q = deque()

for y in range(N):
  for x in range(M):
    if tomato_map[y][x] == 1:
      q.append((y, x))


while q:
  cy, cx = q.popleft()
  for dir in range(4):
    ey = cy + dy[dir]
    ex = cx + dx[dir]
    if 0 <= ey < N and 0 <= ex < M:
      if not tomato_map[ey][ex]:
        tomato_map[ey][ex] = tomato_map[cy][cx] + 1
        q.append((ey, ex))

result = 0
for row in tomato_map:
    if 0 in row:
        print(-1)
        break
    result = max(result, max(row))
else:
    print(result - 1)
