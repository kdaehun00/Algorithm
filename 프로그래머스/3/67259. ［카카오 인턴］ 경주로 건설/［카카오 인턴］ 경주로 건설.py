from collections import deque

def solution(board):
    n = len(board)
    INF = float('inf')
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    cost = [[[INF] * 4 for _ in range(n)] for _ in range(n)]
    
    q = deque()
    for i in range(4):
        cost[0][0][i] = 0
    q.append((0, 0, -1, 0))

    while q:
        y, x, prev_dir, total_cost = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == 0:
                new_cost = total_cost + (100 if prev_dir == -1 or prev_dir == i else 600)

                if cost[ny][nx][i] > new_cost:
                    cost[ny][nx][i] = new_cost
                    q.append((ny, nx, i, new_cost))

    return min(cost[n-1][n-1])