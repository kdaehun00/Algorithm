import sys

input = sys.stdin.readline

expr = input().strip()
parts = expr.split('-')

initial = sum(map(int, parts[0].split('+')))

for part in parts[1:]:
  initial -= sum(map(int, part.split('+')))

print(initial)