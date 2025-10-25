"""
주사위 절반 뽑는 방법 -> 최악의 경우 10C5 -> 9 x 2 x 7 x 2 -> 250가지 정도
뽑은 뒤 5가지의 주사위를 1개씩 뽑을 확률
-> 승 무 패를 모두 db에 기록해놓는다. -> 승만 기록해서 가장 많은 값 출력.
"""
from itertools import combinations, product
import bisect

def solution(dice):
    n = len(dice)
    dice_idx = list(range(n))
    max_win = -1
    answer = []
    
    for comb in combinations(dice_idx, n//2):
        A_team = list(comb)
        B_team = [i for i in dice_idx if i not in A_team]
        
        A_list = [dice[i] for i in A_team]
        B_list = [dice[i] for i in B_team]
        
        A_sum = [sum(list_sum) for list_sum in product(*A_list)]
        B_sum = [sum(list_sum) for list_sum in product(*B_list)]
        
        B_sum.sort()
        
        win_count = 0
        
        for a in A_sum:
            idx = bisect.bisect_left(B_sum, a)
            win_count += idx
                
        if max_win < win_count:
            max_win = win_count
            answer = comb
        
    return [i+1 for i in answer]