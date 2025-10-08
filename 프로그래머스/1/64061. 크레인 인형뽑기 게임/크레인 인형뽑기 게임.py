def solution(board, moves):
    answer = 0
    basket = []

    for move in moves:
        for y in range(len(board)):
            if board[y][move-1] != 0:
                doll = board[y][move-1]
                board[y][move-1] = 0
                if basket and basket[-1] == doll:
                    basket.pop()
                    answer += 2
                else:
                    basket.append(doll)
                break

    return answer