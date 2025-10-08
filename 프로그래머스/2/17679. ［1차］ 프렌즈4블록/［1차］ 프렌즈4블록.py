def solution(m, n, board):
    count = 0
    board = [list(data) for data in board]
    
    while True:
        remove = set()
        
        for y in range(m-1):
            for x in range(n-1):
                if board[y][x] != ' ' and board[y][x] == board[y][x+1] == board[y+1][x] == board[y+1][x+1]:
                    remove.add((y, x))
                    remove.add((y, x+1))
                    remove.add((y+1, x))
                    remove.add((y+1, x+1))
        if not remove:
            break
            
        for y, x in remove:
            board[y][x] = ' '
        
        count += len(remove)
        
        for x in range(n):
            stack = [board[y][x] for y in range(m) if board[y][x] != ' ']
            
            for y in range(m-1, -1, -1):
                board[y][x] = stack.pop() if stack else ' '
            
    return count