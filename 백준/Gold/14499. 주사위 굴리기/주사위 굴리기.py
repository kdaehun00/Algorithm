"""
N, M - 지도의 세로, 가로
x, y - 주사위의 좌표
K - 명령의 갯수
1, 2, 3, 4 -> 동, 서, 북, 남
"""
import sys

input = sys.stdin.readline

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

N, M, y, x, K = map(int, input().split())
map_arr = [list(map(int, input().split())) for _ in range(N)]
move = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0 ,0]

def roll(dir, dice):
  bottom, top, east, west, south, north = dice
  if dir == 0:
    return [east, west, top, bottom, south, north]
  elif dir == 1:
    return [west, east, bottom, top, south, north]
  elif dir == 2:
    return [north, south, east, west, bottom, top]
  elif dir == 3:
    return [south, north, east, west, top, bottom]

for cmd in move:
  dir = cmd - 1
  ny = y + dy[dir]
  nx = x + dx[dir]

  if not (0 <= ny < N and 0 <= nx < M):
    continue

  y, x = ny, nx
  dice = roll(dir, dice)

  if not map_arr[y][x]:
    map_arr[y][x] = dice[0]
  else:
    dice[0] = map_arr[y][x]
    map_arr[y][x] = 0

  print(dice[1])