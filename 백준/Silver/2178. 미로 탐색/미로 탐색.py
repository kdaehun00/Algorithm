"""
1. 아이디어
bfs
숫자가 더 작으면 바꿔치기
숫자가 크면 그대로

2. 시간 복잡도
O(E)
E = 4 * 100 * 100

3. 변수
map = int [][] 실제 지도
cnt = int [][] 값 세는 곳
"""

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]
chk = [[0]*M for _ in range(N)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y, x):
    q = deque()
    q.append((y, x))
    chk[y][x] = 1

    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<N and 0<=nx<M:
                if maze[ny][nx] == 1 and chk[ny][nx] == 0:
                    chk[ny][nx] = chk[ey][ex] + 1
                    q.append((ny, nx))
bfs(0, 0)
print(chk[N-1][M-1])
