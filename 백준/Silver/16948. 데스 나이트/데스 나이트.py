import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
r1, c1, r2, c2 = map(int, input().split())

dy = [-2, -2, 0, 0, 2, 2]
dx = [-1, 1, -2, 2, -1, 1]

min_dist = 10**10

def bfs():
  visited = [[-1] * N for _ in range(N)]
  q = deque()
  q.append((r1, c1))
  visited[r1][c1] = 0

  while q:
    y, x = q.popleft()
    if y == r2 and x == c2:
      return visited[y][x]

    for i in range(6):
      ny = y + dy[i]
      nx = x + dx[i]

      if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == -1:
        visited[ny][nx] = visited[y][x] + 1
        q.append((ny, nx))
  return -1

print(bfs())