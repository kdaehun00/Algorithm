import sys

input = sys.stdin.readline

N = int(input())
road_map = [input().split() for _ in range(N)]

max_val = -float('inf')
min_val = float('inf')

def calc(a, op, b):
  if op == '+': return a + b
  if op == '-': return a - b
  if op == '*': return a * b

dy = [1, 0]
dx = [0, 1]

def dfs(y, x, cur_val, op):
  global max_val, min_val
  if x == N - 1 and y == N - 1:
    max_val = max(max_val, cur_val)
    min_val = min(min_val, cur_val)
    return
  for i in range(2):
    ny = y + dy[i]
    nx = x + dx[i]
    if 0 <= ny < N and 0 <= nx < N:
      cell = road_map[ny][nx]
      if cell in '+-*':
        dfs(ny, nx, cur_val, cell)
      else:
        val = int(cell)
        if op is None:
          dfs(ny, nx, val, None)
        else:
          dfs(ny, nx, calc(cur_val, op, val), None)

dfs(0, 0, int(road_map[0][0]), None)
print(max_val, min_val)