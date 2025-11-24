from itertools import combinations

def solution(n, q, ans):
    count = 0
    
    for code in combinations(range(1, n+1), 5):
        ok = True
        
        for q_i, a_i in zip(q, ans):
            if len(set(code) & set(q_i)) != a_i:
                ok = False
                break
        
        if ok:
            count += 1
    
    return count