"""
P - 응시자, O - 빈테이블, X - 파티션
"""
def solution(places):
    answer = []
    # 직선
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    #대각선
    qy = [-1, 1, -1, 1]
    qx = [-1, 1, 1, -1]
    
    def dfs(place, y, x):
        nonlocal dy, dx, qy, qx
        # 상하좌우부터 체크. -> 사람이 있으면 바로 return false, 책상이면 한 칸 더 뒤로 보기. 벽이면 ok
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < 5 and 0 <= nx < 5:
                if place[ny][nx] == "P":
                    return 0
                elif place[ny][nx] == "O":
                    ny += dy[i]
                    nx += dx[i]
                    if 0 <= ny < 5 and 0 <= nx < 5 and place[ny][nx] == "P":
                        return 0
                else:
                    continue
                    
        # 대각선 체크
        for j in range(4):
            zy = y + qy[j]
            zx = x + qx[j]
            if 0 <= zy < 5 and 0 <= zx < 5:
                if place[zy][zx] == "P":
                    if place[zy][x] != "X" or place[y][zx] != "X":
                        return 0
        return 1
    
    for place in places:
        ok = 1
        for y in range(5):
            for x in range(5):
                if place[y][x] == "P":
                    if not dfs(place, y, x):
                        ok = 0
                        break
            if not ok:
                break
        answer.append(ok)
    return answer