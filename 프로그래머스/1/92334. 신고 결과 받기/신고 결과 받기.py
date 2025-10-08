from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    report_db = defaultdict(list)
    db = defaultdict(int)
    
    report = list(set(report))
    
    for log in report:
        a, b = log.split()
        report_db[a].append(b)
        db[b] += 1
        
    for member in id_list:
        count = 0
        for report_member in report_db[member]:
            if db[report_member] >= k:
                count += 1
        
        answer.append(count)
        
    return answer