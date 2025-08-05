import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
ice_map = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

def bfs():
    chk = [[False] * M for _ in range(N)]
    count = 0
    for y in range(N):
        for x in range(M):
            if ice_map[y][x] > 0 and not chk[y][x]:
                count += 1
                if count >= 2:
                    return count
                q = deque()
                q.append((y, x))
                chk[y][x] = True
                while q:
                    cy, cx = q.popleft()
                    for i in range(4):
                        ny = cy + dy[i]
                        nx = cx + dx[i]
                        if 0 <= ny < N and 0 <= nx < M:
                            if ice_map[ny][nx] > 0 and not chk[ny][nx]:
                                chk[ny][nx] = True
                                q.append((ny, nx))
    return count

def melt_ice():
    melt = [[0] * M for _ in range(N)]
    for y in range(N):
        for x in range(M):
            if ice_map[y][x] > 0:
                cnt = 0
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if 0 <= ny < N and 0 <= nx < M and ice_map[ny][nx] == 0:
                        cnt += 1
                melt[y][x] = cnt

    for y in range(N):
        for x in range(M):
            ice_map[y][x] = max(0, ice_map[y][x] - melt[y][x])

year = 0
while True:
    parts = bfs()
    if parts >= 2:
        print(year)
        break
    if parts == 0:
        print(0)
        break
    melt_ice()
    year += 1