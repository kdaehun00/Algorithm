"""
비교 조건
1. 더 많이 준 사람이 받는다.
2. 선물 지수가 더 작은 사람이 받는다.

선물 지수 -> 준 수 - 받은 수
"""
from collections import defaultdict

def solution(friends, gifts):
    db = defaultdict(lambda: defaultdict(int))
    gift_db = defaultdict(int)
    answer = 0
    
    for log in gifts:
        a, b = log.split()
        db[a][b] += 1
        gift_db[a] += 1
        gift_db[b] -= 1
    
    for me in friends:
        count = 0
        for you in friends:
            if me == you:
                continue
            else:
                if db[me][you] > db[you][me]:
                    count += 1
                elif db[me][you] == db[you][me]:
                    if gift_db[me] > gift_db[you]:
                        count += 1
        answer = max(answer, count)
    return answer