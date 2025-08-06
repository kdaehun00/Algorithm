"""
N - 화의의 개수 ( 1 <= N <= 100,000 )
"""
import sys

input = sys.stdin.readline

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
last_end_time = 0

for start_time, end_time in meetings:
  if start_time >= last_end_time:
    count += 1
    last_end_time = end_time

print(count)