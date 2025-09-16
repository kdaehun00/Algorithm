"""
A - 6, B - 12, C - 3

출력: 파기해야할 개인정보 번호
"""
from collections import defaultdict
def solution(today, terms, privacies):
    def to_days(date_str):
        y, m, d = map(int, date_str.split("."))
        return y*12*28 + m*28 + d
    
    today_days = to_days(today)
    db = defaultdict(int)
    
    for term in terms:
        data_type, data_period = term.split()
        db[data_type] = int(data_period)
    
    answer = []
    for i in range(len(privacies)):
        date, data_type = privacies[i].split()
        days = to_days(date) + (db[data_type] * 28)
        if days <= today_days:
            answer.append(i+1)
        
    return answer