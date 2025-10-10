from collections import deque

def solution(m, n, board):
    answer = 0
    board = [list(data) for data in board]
    
    while True:
        remove = set()
        for y in range(m-1):
            for x in range(n-1):
                if board[y][x] != " " and board[y][x] == board[y][x+1] == board[y+1][x] == board[y+1][x+1]:
                    remove.update({(y, x), (y, x+1), (y+1, x), (y+1, x+1)})
                    
        if not remove:
            break
            
        for y, x in remove:
            board[y][x] = " "
        
        answer += len(remove)
        
        for x in range(n):
            move_list = deque()
            for y in range(m-1, -1, -1):
                if board[y][x] != " ":
                    move_list.append(board[y][x])
            for y in range(m-1, -1, -1):
                board[y][x] = move_list.popleft() if move_list else " "
                
    return answer