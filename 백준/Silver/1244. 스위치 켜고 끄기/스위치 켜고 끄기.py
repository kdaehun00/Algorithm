"""
남학생 - 부여받은 수의 배수를 무조건 바꿈
야학생 - 부여받은 수를 기준으로 대칭이면 바꿈 / 양옆이 대칭이 아니면 바로 멈추고 자기꺼만 바꿈
N - 스위치 개수 ( 0 < N <= 100 )
M - 학생 수 ( 0 < M <= 100 )
남학생 - 1
여학생 - 2

M 만큼 for문
  if 남/여
    남 -> N 리스트 돌며 변환
    여 -> 투포인터로 변환

-> 시간복잡도는 O(N*M) = 10^4 - 충분
"""
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
switch_status = deque(map(int, input().split()))
switch_status.appendleft(0)
M = int(input())
students = [list(map(int, input().split())) for _ in range(M)]

for i in students:
  gender, num = i
  if gender == 1:
    for ch_idx in range(num, N+1, num):
      switch_status[ch_idx] = switch_status[ch_idx] ^ 1
  if gender == 2:
    switch_status[num] = switch_status[num] ^ 1
    min_size = min(num-1, N-num)
    for idx in range(1, min_size + 1):
      if switch_status[num - idx] != switch_status[num + idx]:
        break

      switch_status[num - idx] = switch_status[num + idx] = switch_status[num - idx] ^ 1

switch_status.popleft()
for i in range(N):
  print(switch_status[i], end=' ')
  if (i + 1) % 20 == 0:
    print()