from collections import defaultdict
from itertools import combinations
import bisect

def solution(info, query):
    answer = []
    db = defaultdict(list)
    stack_index = [x for x in range(4)]
    
    for employee in info:
        data_list = list(employee.split())
        stack, score = data_list[:-1], int(data_list[-1])
        
        for i in range(5):
            for j in combinations(stack_index, i):
                temp = stack.copy()
                for change_index in j:
                    temp[change_index] = "-"
                db[" ".join(temp)].append(score)
    
    for key in db:
        db[key].sort()
        
    for data in query:
        data = data.replace(" and", "")
        find_list = list(data.split())
        stack, score = " ".join(find_list[:-1]), int(find_list[-1])
        
        scores = db.get(stack, [])
        idx = bisect.bisect_left(scores, score)
        answer.append(len(scores) - idx)
        
    return answer