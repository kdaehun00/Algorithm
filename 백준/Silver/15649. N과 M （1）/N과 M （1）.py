from itertools import permutations
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

num_list = [x for x in range(1, n+1)]

for data in permutations(num_list, m):
  data = list(data)

  if len(data) == 1:
    print(data[0])
  else:
    print(" ".join(map(str, data)))