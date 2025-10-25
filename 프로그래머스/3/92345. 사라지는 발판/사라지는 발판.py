import copy

def solution(board, aloc, bloc):
    R, C = len(board), len(board[0])
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    
    def dfs(cur_r, cur_c, opp_r, opp_c, b):
        if b[cur_r][cur_c] == 0:
            return (False, 0)  # 현재 플레이어 이동 불가 → 패배
        
        win = False
        max_cnt = 0
        min_cnt = float('inf')
        
        for dr, dc in directions:
            nr, nc = cur_r + dr, cur_c + dc
            if 0 <= nr < R and 0 <= nc < C and b[nr][nc] == 1:
                b[cur_r][cur_c] = 0  # 이동하면 발판 사라짐
                opp_win, cnt = dfs(opp_r, opp_c, nr, nc, b)
                b[cur_r][cur_c] = 1  # 상태 복구
                
                if not opp_win:  # 상대가 지면 현재 승리
                    win = True
                    min_cnt = min(min_cnt, cnt+1)
                else:           # 상대가 이기면 현재 패배
                    max_cnt = max(max_cnt, cnt+1)
        
        if win:
            return (True, min_cnt)
        else:
            return (False, max_cnt)
    
    _, answer = dfs(aloc[0], aloc[1], bloc[0], bloc[1], copy.deepcopy(board))
    return answer