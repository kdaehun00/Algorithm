import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]

cleaner = []
for i in range(R):
    if room[i][0] == -1:
        cleaner.append(i)
upper, lower = cleaner

dirs = [(-1,0),(1,0),(0,-1),(0,1)]

def spread():
    temp = [[0]*C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if room[r][c] > 0:
                amount = room[r][c] // 5
                cnt = 0
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < R and 0 <= nc < C and room[nr][nc] != -1:
                        temp[nr][nc] += amount
                        cnt += 1
                room[r][c] -= amount * cnt
    for r in range(R):
        for c in range(C):
            room[r][c] += temp[r][c]

def purify():
    for r in range(upper-1,0,-1):
        room[r][0] = room[r-1][0]
    for c in range(C-1):
        room[0][c] = room[0][c+1]
    for r in range(upper):
        room[r][C-1] = room[r+1][C-1]
    for c in range(C-1,1,-1):
        room[upper][c] = room[upper][c-1]
    room[upper][1] = 0

    for r in range(lower+1,R-1):
        room[r][0] = room[r+1][0]
    for c in range(C-1):
        room[R-1][c] = room[R-1][c+1]
    for r in range(R-1,lower,-1):
        room[r][C-1] = room[r-1][C-1]
    for c in range(C-1,1,-1):
        room[lower][c] = room[lower][c-1]
    room[lower][1] = 0

for _ in range(T):
    spread()
    purify()

ans = 0
for r in range(R):
    for c in range(C):
        if room[r][c] > 0:
            ans += room[r][c]
print(ans)