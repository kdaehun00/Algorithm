"""
우선순위: 보낸 선물 수 > 선물 지수 > 주고 받지 X

선물 지수 = 친구들에게 준 선물 수 - 친구들에게 받은 선물 수

출력: 선물을 가장 많이 받을 친구의 '선물 수'

1. dict를 만들어서 안에 준 사람을 저장, list에 선물 지수 +1
2. gift를 한 바퀴 돌면서 준 사람과 받은 사람의 수를 비교
3. result에 + 1
"""
from collections import defaultdict

def solution(friends, gifts):
    n = len(friends)
    db = defaultdict(lambda: defaultdict(int))
    gift_index = defaultdict(int)
    received = defaultdict(int)
    
    for gift in gifts:
        a, b = gift.split()
        db[a][b] += 1
        gift_index[a] += 1
        gift_index[b] -= 1
        
    for i in range(n):
        for j in range(i+1, n):
            a, b = friends[i], friends[j]
            a2b, b2a = db[a][b], db[b][a]

            if a2b > b2a:         # a가 더 줌 → a가 선물 받을 차례
                received[a] += 1
            elif b2a > a2b:       # b가 더 줌 → b가 선물 받을 차례
                received[b] += 1
            else:                 # 같으면 선물 지수 비교
                if gift_index[a] > gift_index[b]:
                    received[a] += 1
                elif gift_index[b] > gift_index[a]:
                    received[b] += 1
    return max(received.values(), default=0)