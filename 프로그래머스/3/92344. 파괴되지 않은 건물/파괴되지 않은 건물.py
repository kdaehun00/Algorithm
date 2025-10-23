def solution(board, skill):
    n, m = len(board), len(board[0])
    diff = [[0]*(m+1) for _ in range(n+1)]
    
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1: degree = -degree
        diff[r1][c1] += degree
        diff[r1][c2+1] -= degree
        diff[r2+1][c1] -= degree
        diff[r2+1][c2+1] += degree

    for y in range(n):
        for x in range(1, m):
            diff[y][x] += diff[y][x-1]
    
    for x in range(m):
        for y in range(1, n):
            diff[y][x] += diff[y-1][x]
    
    answer = 0
    for y in range(n):
        for x in range(m):
            if board[y][x] + diff[y][x] > 0:
                answer += 1
    return answer