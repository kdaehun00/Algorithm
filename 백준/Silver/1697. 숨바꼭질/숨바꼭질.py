"""
N - 수빈이의 현재 점
K - 동생의 점
"""

import sys
from collections import deque

input = sys.stdin.readline
MAX = 100001
N, K = map(int, input().split())
move = [-1] * MAX

def bfs(start):
  q = deque()
  q.append(start)
  move[start] = 0

  while q:
    now = q.popleft()
    if now == K:
      return move[now]

    for nxt in (now + 1, now -1, now*2):
      if 0 <= nxt < MAX and move[nxt] == -1:
        move[nxt] = move[now] + 1
        q.append(nxt)

print(bfs(N))