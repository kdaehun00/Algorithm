from collections import defaultdict
    
def solution(record):
    
    db = defaultdict(str)
    answer = []
    record_lst = []
    
    for part in record:
        data = part.split()
        status = data[0]
        if status == "Enter":
            uid = data[1]
            name = data[2]
            db[uid] = name
            answer.append((uid, "님이 들어왔습니다."))
            
        elif status == "Leave":
            uid = data[1]
            answer.append((uid, "님이 나갔습니다."))
            
        elif status == "Change":
            uid = data[1]
            name = data[2]
            db[uid] = name
            
    for lst in answer:
        name = db[lst[0]]
        record_lst.append(name + lst[1])
        
    return record_lst