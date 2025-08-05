import sys
from collections import deque

input = sys.stdin.readline

wheels = [deque(list(map(int, input().rstrip()))) for _ in range(4)]
N = int(input())
commands = [list(map(int, input().split())) for _ in range(N)]

def turn_wheel(wheel_idx, direction):
  if direction == 1:
    wheels[wheel_idx].rotate(1)
  else:
    wheels[wheel_idx].rotate(-1)

for wheel_num, dir in commands:
    wheel_num -= 1
    directions = [0]*4
    directions[wheel_num] = dir

    for i in range(wheel_num-1, -1, -1):
        if wheels[i][2] != wheels[i+1][6]:
            directions[i] = -directions[i+1]
        else:
            break

    for i in range(wheel_num+1, 4):
        if wheels[i-1][2] != wheels[i][6]:
            directions[i] = -directions[i-1]
        else:
            break

    for i in range(4):
        if directions[i] != 0:
            turn_wheel(i, directions[i])

result = 0
for i in range(4):
    if wheels[i][0] == 1:
        result += 2 ** i

print(result)