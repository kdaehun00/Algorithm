from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    block_list = []
    db = defaultdict(int)
    result_db = defaultdict(list)
    
    set_report = list(set(report))
    
    for data in set_report:
        a, b = data.split()
        db[b] += 1
        result_db[a].append(b)
    
    for key, value in db.items():
        if value >= k:
            block_list.append(key)
    
    for user in id_list:
        count = 0
        for block in result_db[user]:
            if db[block] >= k:
                count+=1
        answer.append(count)
        
    return answer