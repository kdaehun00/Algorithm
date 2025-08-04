import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
  p = input().strip()
  n = int(input())
  arr_input = input().strip()

  if n == 0:
    arr = deque()
  else :
    arr = deque(map(int, arr_input[1: -1].split(',')))

  reverse = False
  error = False

  for cmd in p:
    if cmd == 'R':
      reverse = not reverse
    else :
      if not arr:
        error = True
        break
      if reverse :
        arr.pop()
      else :
        arr.popleft()

  if error:
    print('error')
  else:
    if reverse:
      arr.reverse()
    print("[" + ",".join(map(str, arr)) + "]")