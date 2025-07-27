import sys
from collections import deque

input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(y, x, lettuce_map, chk, N, M):
    q = deque()
    q.append((y, x))
    chk[y][x] = True

    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ey = cy + dy[i]
            ex = cx + dx[i]

            if 0 <= ey < N and 0 <= ex < M:
                if lettuce_map[ey][ex] and not chk[ey][ex]:
                    chk[ey][ex] = True
                    q.append((ey, ex))

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())

    lettuce_map = [[0] * M for _ in range(N)]
    chk = [[False] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        lettuce_map[y][x] = 1

    worm_count = 0
    for y in range(N):
        for x in range(M):
            if lettuce_map[y][x] and not chk[y][x]:
                bfs(y, x, lettuce_map, chk, N, M)
                worm_count += 1

    print(worm_count)