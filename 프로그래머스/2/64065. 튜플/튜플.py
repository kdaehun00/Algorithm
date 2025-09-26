"""
"""
from collections import defaultdict

def solution(s):
    answer = []
    db = defaultdict(int)

    s1 = s[2:len(s)-2].split('},{')
    s_list = list(map(int ,item.split(",")) for item in s1)
    
    for data in s_list:
        for num in data:
            db[num] += 1
    
    sorted_db = sorted(db.items(), key=lambda x: -x[1])
    
    for key, _ in sorted_db:
        answer.append(key)

    return answer