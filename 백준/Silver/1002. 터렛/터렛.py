import sys
import math

input = sys.stdin.readline

T = int(input())

for _ in range(T):
  x1, y1, r1, x2, y2, r2 = map(int, input().split())

  dx = x2 - x1
  dy = y2 - y1
  d = math.hypot(dx, dy)

  if d == 0:
    if r1 == r2:
      print(-1)
    else:
      print(0)
  else:
    if d > r1 + r2:
      print(0)
    elif d == r1 + r2:
      print(1)
    elif abs(r1 - r2) < d < r1 + r2:
      print(2)
    elif d == abs(r1 - r2):
      print(1)
    else:
      print(0)