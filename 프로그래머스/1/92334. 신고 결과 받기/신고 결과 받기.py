from collections import defaultdict

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    db = defaultdict(int)
    
    set_report = list(set(report))
    
    for data in set_report:
        a, b = data.split()
        db[b] += 1
    
    for data in set_report:
        a, b = data.split()
        if db[b] >= k:
            answer[id_list.index(a)] += 1
            
    return answer