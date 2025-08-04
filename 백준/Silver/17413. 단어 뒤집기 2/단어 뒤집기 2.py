import sys
from collections import deque

input = sys.stdin.readline

S = input().rstrip()
result = ''
stack = []
in_tag = False

for ch in S:
  if ch == '<':
    while stack:
      result += stack.pop()
    in_tag = True
    result += ch
  elif ch == '>':
    in_tag = False
    result += ch
  elif in_tag:
    result += ch
  elif ch == ' ':
    while stack:
      result += stack.pop()
    result += ' '
  else:
    stack.append(ch)

while stack:
    result += stack.pop()

print(result)